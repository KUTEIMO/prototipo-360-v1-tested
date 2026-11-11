/* global URL, Headers, Response */
/**
 * Cloudflare Pages Function — virtual multi-tenant router & HTTP hardening for Orbe360.
 * Paired with dist/_routes.json so /media/*, /css/*, /src/*, /vendors/*, and assets
 * bypass this function completely (zero worker quota used on panoramas/audio).
 */

const SLUG_RE = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

const RESERVED = new Set([
  "plataforma",
  "control-web",
  "panoramas",
  "assets",
  "media",
  "css",
  "src",
  "vendors",
  "images",
  "tests",
  "docs",
  "scripts",
  "reports",
  "node_modules",
  "convex",
  "playwright-report",
  "test-results",
  "backups",
  "dist",
  "deploy",
  "functions",
]);

const BLOCKED_ROOT_FILES = new Set([
  ".env",
  ".env.local",
  ".gitignore",
  "package.json",
  "package-lock.json",
  "convex.json",
  "playwright.config.js",
  "eslint.config.mjs",
  "skills-lock.json",
  "agents.md",
  "claude.md",
  "changelog.md",
  "license",
  "leeme.md",
  "readme.md",
  "backlog.md",
  "ubicacion_y_archivo.md",
  "audit-runner.js",
  "instrumento_auditoria_v1.json",
  "demo.html",
  "demo-report.html",
  "styles(old_together).css",
  "config.local.js",
  "orbe-config.local.js",
]);

function securityHeaders(extra = {}) {
  return {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "SAMEORIGIN",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), geolocation=(), microphone=(self)",
    "Cache-Control": "no-store, max-age=0",
    ...extra,
  };
}

async function fetchHtml(env, origin, assetPath) {
  let res = await env.ASSETS.fetch(new URL(assetPath, origin));
  if (res.status >= 300 && res.status < 400) {
    const loc = res.headers.get("location");
    if (loc) {
      res = await env.ASSETS.fetch(new URL(loc, origin));
    }
  }
  const headers = new Headers(res.headers);
  const sec = securityHeaders();
  for (const [k, v] of Object.entries(sec)) headers.set(k, v);
  headers.set("Content-Type", "text/html; charset=utf-8");
  return new Response(res.body, { status: res.status === 404 ? 404 : 200, headers });
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const path = url.pathname;
  const clean = path.replace(/^\/+|\/+$/g, "");
  const parts = clean ? clean.split("/") : [];
  const firstLower = (parts[0] || "").toLowerCase();

  // 1. Block internal repo files, env leaks, dotfiles, course archives, and retired legacy /panoramas /assets paths.
  if (
    BLOCKED_ROOT_FILES.has(clean.toLowerCase()) ||
    clean.toLowerCase().startsWith(".env") ||
    firstLower.startsWith(".") ||
    firstLower === "convex" ||
    firstLower === "docs" ||
    firstLower === "dist" ||
    firstLower === "scripts" ||
    firstLower === "tests" ||
    firstLower === "backups" ||
    firstLower === "deploy" ||
    firstLower === "functions" ||
    firstLower === "reports" ||
    firstLower === "node_modules" ||
    firstLower.startsWith("entregables-") ||
    firstLower === "_restos_exras_bloqueados"
  ) {
    return new Response("Not Found", { status: 404, headers: securityHeaders({ "Content-Type": "text/plain; charset=utf-8" }) });
  }
  if (firstLower === "panoramas" || firstLower === "assets") {
    return new Response("Legacy media path disabled", { status: 410, headers: securityHeaders({ "Content-Type": "text/plain; charset=utf-8" }) });
  }

  // 2. Landing at root /; legacy /plataforma(/index.html) -> 302 /
  if (path === "/" || path === "/index.html") {
    return fetchHtml(env, url.origin, "/index.html");
  }
  if (/^\/plataforma(\/|\/index\.html)?$/i.test(path)) {
    return Response.redirect(new URL("/", url.origin), 302);
  }
  if (/^\/[^/]+\/[^/]+\/plataforma\/index\.html$/i.test(path)) {
    return Response.redirect(new URL("/", url.origin), 302);
  }
  if (/^\/[^/]+\/[^/]+\/plataforma\/login\.html$/i.test(path)) {
    const target = new URL("/plataforma/login.html", url.origin);
    target.search = url.search;
    return Response.redirect(target, 302);
  }

  // 3. Direct /plataforma/*.html pages (login, org-admin, superadmin, accesibilidad, legales)
  if (/^\/plataforma\/[^/]+\.html$/i.test(path)) {
    return fetchHtml(env, url.origin, path);
  }

  // 4. Org-level admin: /{org}/org-admin.html (and nested redirect)
  if (parts.length === 2 && parts[1] === "org-admin.html" && SLUG_RE.test(parts[0]) && !RESERVED.has(parts[0])) {
    return fetchHtml(env, url.origin, "/plataforma/org-admin.html");
  }
  if (parts.length === 3 && parts[2] === "org-admin.html" && SLUG_RE.test(parts[0]) && SLUG_RE.test(parts[1]) && !RESERVED.has(parts[0])) {
    const redir = new URL(`/${parts[0]}/org-admin.html`, url.origin);
    redir.search = url.search;
    return Response.redirect(redir, 302);
  }

  // 5. Control Web under tour prefix: /{org}/{tour}/control-web(/...)
  if (
    parts.length >= 3 &&
    parts[2] === "control-web" &&
    SLUG_RE.test(parts[0]) &&
    SLUG_RE.test(parts[1]) &&
    !RESERVED.has(parts[0]) &&
    !RESERVED.has(parts[1])
  ) {
    if (parts.length === 3 && !path.endsWith("/")) {
      const slashUrl = new URL(`${path}/`, url.origin);
      slashUrl.search = url.search;
      return Response.redirect(slashUrl, 301);
    }
    if (parts.length === 3 || (parts.length === 4 && parts[3] === "index.html")) {
      return fetchHtml(env, url.origin, "/control-web/index.html");
    }
    const subAsset = `/control-web/${parts.slice(3).join("/")}`;
    return env.ASSETS.fetch(new URL(subAsset, url.origin));
  }

  // 6. Canonical tour viewer: /{org}/{tour} or /{org}/{tour}/
  if (
    parts.length === 2 &&
    SLUG_RE.test(parts[0]) &&
    SLUG_RE.test(parts[1]) &&
    !RESERVED.has(parts[0]) &&
    !RESERVED.has(parts[1])
  ) {
    if (!path.endsWith("/")) {
      const slashUrl = new URL(`${path}/`, url.origin);
      slashUrl.search = url.search;
      return Response.redirect(slashUrl, 301);
    }
    return fetchHtml(env, url.origin, "/viewer.html");
  }

  // 7. Fall through to static asset bucket (e.g., /control-web/, /favicon.ico, etc.)
  return env.ASSETS.fetch(request);
}
