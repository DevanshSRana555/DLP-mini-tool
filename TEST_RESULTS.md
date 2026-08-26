# Test Results

## Automated environment check

The project files were syntax-compiled successfully with Python `compileall`.

Core detector/security smoke tests also passed, including:

- AWS key detection
- Private-key marker detection
- Email/phone detection
- Severity summary
- Secret masking in previews
- Path-traversal-safe filenames
- File-extension allowlist

## Full pytest suite

The full FastAPI test suite could not be executed in this environment because external Python packages (`fastapi`, `pytest`, etc.) are not installed and this environment has no package-index/network access. The failure was environmental rather than an application test failure.

To run the complete suite on a normal development machine:

```bash
pip install -r requirements.txt
pytest -q
```
