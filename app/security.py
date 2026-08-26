from fastapi import Request
from fastapi.responses import JSONResponse

MAX_FILE_BYTES = 2 * 1024 * 1024
ALLOWED_EXTENSIONS = {".txt", ".csv", ".log", ".json", ".md", ".xml", ".html", ".yaml", ".yml"}

def safe_filename(filename: str | None) -> str:
    name = (filename or "unnamed").replace("\\", "/").split("/")[-1]
    name = "".join(ch for ch in name if ch.isprintable() and ch not in "\x00\r\n")
    return name[:120] or "unnamed"

def is_allowed_filename(filename: str) -> bool:
    from pathlib import Path
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

async def security_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Content-Security-Policy"] = "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    response.headers["Cache-Control"] = "no-store"
    return response

def size_limit_response():
    return JSONResponse({"detail": "File exceeds the 2 MiB limit."}, status_code=413)
