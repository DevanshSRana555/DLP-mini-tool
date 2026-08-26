from app.security import safe_filename,is_allowed_filename

def test_path_traversal_is_removed():
    assert safe_filename("../../secret.txt")=="secret.txt"
    assert safe_filename(r"..\..\secret.txt")=="secret.txt"

def test_extension_allowlist():
    assert is_allowed_filename("report.csv")
    assert not is_allowed_filename("payload.exe")
