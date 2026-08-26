from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from .detector import scan_text, summary
from .security import MAX_FILE_BYTES, is_allowed_filename, safe_filename, security_headers_middleware, size_limit_response

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
app = FastAPI(title="DLP Mini Tool", version="1.0.0", docs_url="/docs", redoc_url=None)
app.middleware("http")(security_headers_middleware)

@app.get("/", include_in_schema=False)
async def index():
    return FileResponse(STATIC_DIR / "index.html")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/api/scan")
async def scan(file: UploadFile = File(...)):
    filename = safe_filename(file.filename)
    if not is_allowed_filename(filename):
        return JSONResponse({"detail": "Unsupported file type. Allowed: txt, csv, log, json, md, xml, html, yaml, yml."}, status_code=415)
    data = await file.read(MAX_FILE_BYTES + 1)
    if len(data) > MAX_FILE_BYTES:
        return size_limit_response()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return JSONResponse({"detail": "Only UTF-8 text files are supported."}, status_code=415)
    findings = scan_text(text)
    return {
        "filename": filename,
        "bytes_scanned": len(data),
        "findings": [f.__dict__ for f in findings],
        "summary": summary(findings),
        "safe_to_share": not any(f.severity in {"critical", "high"} for f in findings),
    }
