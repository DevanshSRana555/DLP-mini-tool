# Data Loss Prevention Mini Tool

A working MVP that scans text-based files for common sensitive-data patterns **before they are uploaded or shared**.

## Features
- FastAPI backend + simple browser UI.
- In-memory scanning; uploaded files are not persisted.
- AWS keys, private keys, JWT-like tokens, email addresses, credit-card-like numbers, phone numbers, and generic API/access/secret keys.
- Severity levels and remediation recommendations.
- Masked match previews so full secrets are not returned.
- 2 MiB upload limit, extension allowlist, UTF-8 validation.
- CSP, `nosniff`, frame denial, referrer/permissions policy, and `no-store` headers.
- Filename sanitization/path-traversal protection.
- Automated tests and a non-root Docker image.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000`. API docs: `/docs`.

## Test
```bash
pytest -q
```

## Docker
```bash
docker build -t dlp-mini-tool .
docker run --rm -p 8000:8000 dlp-mini-tool
```

## API
```bash
curl -F "file=@sample_sensitive.txt" http://127.0.0.1:8000/api/scan
```

## Security notes
This is an MVP, not enterprise DLP. Implemented protections include in-memory processing, size limits, file-extension allowlisting, UTF-8 validation, filename sanitization, masked findings, security headers, and a non-root container.

For production, add authentication/authorization, rate limiting, MIME/content sniffing, archive/parser sandboxing, stronger secret detectors, Luhn validation, audit controls, dependency/SAST/container scanning, TLS, and organization-specific policies.

## Project structure
```text
dlp_mini_tool/
├── app/               # API, detector, security middleware
├── static/             # browser UI
├── tests/              # unit + API tests
├── Dockerfile
├── requirements.txt
├── README.md
└── sample_sensitive.txt
```
