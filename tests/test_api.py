from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def test_health_and_security_headers():
    r=client.get("/health")
    assert r.status_code==200 and r.json()=={"status":"ok"}
    assert r.headers["X-Content-Type-Options"]=="nosniff"
    assert r.headers["X-Frame-Options"]=="DENY"
    assert "frame-ancestors 'none'" in r.headers["Content-Security-Policy"]

def test_scan_clean_file():
    r=client.post("/api/scan",files={"file":("notes.txt",b"hello world","text/plain")})
    assert r.status_code==200 and r.json()["safe_to_share"] is True

def test_scan_sensitive_file():
    r=client.post("/api/scan",files={"file":("config.txt",b"AKIA1234567890ABCDEF","text/plain")})
    assert r.status_code==200 and r.json()["safe_to_share"] is False
    assert r.json()["summary"]["by_severity"]["critical"]==1

def test_rejects_bad_extension():
    r=client.post("/api/scan",files={"file":("malware.exe",b"hello","application/octet-stream")})
    assert r.status_code==415

def test_rejects_oversized_file():
    r=client.post("/api/scan",files={"file":("large.txt",b"x"*(2*1024*1024+1),"text/plain")})
    assert r.status_code==413
