# Test Results

## Automated Environment Check

The project files were successfully syntax-compiled using Python `compileall`.

Core DLP detector and security checks also passed, including:

- AWS key detection
- Private-key marker detection
- Email and phone detection
- Severity summary
- Secret masking in previews
- Path-traversal-safe filename handling
- File-extension allowlist

## Full Pytest Suite

The full pytest suite could not be executed in the available environment because the required external Python packages, including `pytest` and `fastapi`, were not installed, and package installation was not available in that environment.

This means the full test suite is **not being reported as passed**.

To run the complete test suite on a normal development machine:

```bash
pip install -r requirements.txt
pytest -q
