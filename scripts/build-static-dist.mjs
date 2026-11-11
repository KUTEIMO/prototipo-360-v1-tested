#!/usr/bin/env node
/**
 * Build sanitized static distribution bundle in ./dist for production hosting
 * (Cloudflare Pages / Firebase Hosting / Netlify) paired with Convex Cloud.
 *
 * Usage:
 *   ORBE_CONVEX_URL=https://your-deployment.convex.cloud npm run build:prod
 *   node scripts/build-static-dist.mjs --dry-run
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const DIST = path.join(ROOT, "dist");

const argv = new Set(process.argv.slice(2));
const dryRun = argv.has("--dry-run");
const allowLocal = argv.has("--allow-local");
const convexUrl = String(process.env.ORBE_CONVEX_URL || "").trim().replace(/\/$/, "");

if (convexUrl) {
  let parsed;
  try {
    parsed = new URL(convexUrl);
  } catch {
    console.error(`[build:prod] Invalid ORBE_CONVEX_URL: ${convexUrl}`);
    process.exit(1);
  }
  const isLocalHost = parsed.hostname === "127.0.0.1" || parsed.hostname === "localhost";
  if (parsed.protocol !== "https:" && !(allowLocal && isLocalHost)) {
    console.error(`[build:prod] ORBE_CONVEX_URL must use https:// (got ${convexUrl})`);
    process.exit(1);
  }
}

const SKIP_BASENAMES = new Set([
  ".DS_Store",
  "Thumbs.db",
  "Desktop.ini",
  "links de images en internet .txt",
]);

function shouldCopyFile(relPosix) {
  const base = path.posix.basename(relPosix);
  if (SKIP_BASENAMES.has(base)) return false;
  if (base.startsWith(".env")) return false;
  if (relPosix.endsWith(".md")) return false;
  if (relPosix.endsWith(".local.js")) return false;
  return true;
}

function copyDirFiltered(srcDir, dstDir, relPrefix = "") {
  if (!fs.existsSync(srcDir)) return 0;
  let count = 0;
  if (!dryRun) fs.mkdirSync(dstDir, { recursive: true });
  for (const entry of fs.readdirSync(srcDir, { withFileTypes: true })) {
    const rel = relPrefix ? `${relPrefix}/${entry.name}` : entry.name;
    const srcPath = path.join(srcDir, entry.name);
    const dstPath = path.join(dstDir, entry.name);
    if (entry.isDirectory()) {
      count += copyDirFiltered(srcPath, dstPath, rel);
    } else if (shouldCopyFile(rel)) {
      if (!dryRun) {
        fs.copyFileSync(srcPath, dstPath);
      }
      count += 1;
    }
  }
  return count;
}

function buildFirebaseConfig() {
  return {
    hosting: {
      public: ".",
      ignore: ["firebase.json", "**/.*", "**/node_modules/**"],
      redirects: [
        { source: "/plataforma", destination: "/", type: 301 },
        { source: "/plataforma/", destination: "/", type: 301 },
        { source: "/plataforma/index.html", destination: "/", type: 301 },
        {
          source: "/:org/:tour/org-admin.html",
          destination: "/:org/org-admin.html",
          type: 302,
        },
      ],
      rewrites: [
        { source: "/:org/org-admin.html", destination: "/plataforma/org-admin.html" },
        { source: "/:org/:tour/control-web", destination: "/control-web/index.html" },
        { source: "/:org/:tour/control-web/", destination: "/control-web/index.html" },
        { source: "/:org/:tour/control-web/**", destination: "/control-web/index.html" },
        { source: "/:org/:tour", destination: "/viewer.html" },
        { source: "/:org/:tour/", destination: "/viewer.html" },
      ],
      headers: [
        {
          source: "**",
          headers: [
            { key: "X-Content-Type-Options", value: "nosniff" },
            { key: "X-Frame-Options", value: "SAMEORIGIN" },
            { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
            {
              key: "Permissions-Policy",
              value: "camera=(), geolocation=(), microphone=(self)",
            },
          ],
        },
        {
          source: "**/*.html",
          headers: [{ key: "Cache-Control", value: "no-cache" }],
        },
        {
          source: "/media/**",
          headers: [{ key: "Cache-Control", value: "public, max-age=604800" }],
        },
        {
          source: "/vendors/**",
          headers: [{ key: "Cache-Control", value: "public, max-age=604800" }],
        },
      ],
    },
  };
}

const CLOUDFLARE_REDIRECTS = [
  "/plataforma / 301",
  "/plataforma/ / 301",
  "/plataforma/index.html / 301",
  "/:org/org-admin.html /plataforma/org-admin.html 200",
  "/:org/:tour/org-admin.html /:org/org-admin.html 302",
  "/:org/:tour/control-web /:org/:tour/control-web/ 301",
  "/:org/:tour/control-web/ /control-web/index.html 200",
  "/:org/:tour/ /viewer.html 200",
  "/:org/:tour /viewer.html 200",
  "",
].join("\n");

const CLOUDFLARE_HEADERS = [
  "/*",
  "  X-Content-Type-Options: nosniff",
  "  X-Frame-Options: SAMEORIGIN",
  "  Referrer-Policy: strict-origin-when-cross-origin",
  "  Permissions-Policy: camera=(), geolocation=(), microphone=(self)",
  "",
  "/*.html",
  "  Cache-Control: no-cache",
  "",
  "/media/*",
  "  Cache-Control: public, max-age=604800",
  "",
  "/vendors/*",
  "  Cache-Control: public, max-age=604800",
  "",
].join("\n");

if (!dryRun) {
  fs.rmSync(DIST, { recursive: true, force: true });
  fs.mkdirSync(DIST, { recursive: true });
}

let totalFiles = 0;
for (const dir of ["css", "src", "vendors", "plataforma", "control-web", "media"]) {
  totalFiles += copyDirFiltered(path.join(ROOT, dir), path.join(DIST, dir), dir);
}

// Root landing is plataforma/index.html; root viewer sits at /viewer.html so / matches cleanly.
if (!dryRun) {
  fs.copyFileSync(path.join(ROOT, "plataforma", "index.html"), path.join(DIST, "index.html"));
  fs.copyFileSync(path.join(ROOT, "index.html"), path.join(DIST, "viewer.html"));

  const orbeCfgRaw = fs.readFileSync(path.join(ROOT, "orbe-config.js"), "utf8");
  const platCfgRaw = fs.readFileSync(path.join(ROOT, "plataforma", "config.js"), "utf8");
  const injectBanner = convexUrl
    ? `window.__CONVEX_URL__ = window.__CONVEX_URL__ || ${JSON.stringify(convexUrl)};\n`
    : "";
  fs.writeFileSync(path.join(DIST, "orbe-config.js"), `${injectBanner}${orbeCfgRaw}`, "utf8");
  fs.writeFileSync(
    path.join(DIST, "plataforma", "config.js"),
    `${injectBanner}${platCfgRaw}`,
    "utf8"
  );

  fs.writeFileSync(path.join(DIST, "_redirects"), CLOUDFLARE_REDIRECTS, "utf8");
  fs.writeFileSync(path.join(DIST, "_headers"), CLOUDFLARE_HEADERS, "utf8");
  fs.writeFileSync(
    path.join(DIST, "firebase.json"),
    `${JSON.stringify(buildFirebaseConfig(), null, 2)}\n`,
    "utf8"
  );
}
totalFiles += 7;

console.log(
  `[build:prod] ${dryRun ? "Dry-run OK" : "Built"} dist/ (${totalFiles} files${convexUrl ? `, Convex=${convexUrl}` : ", no Convex URL baked in"}).`
);

