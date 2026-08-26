from app.detector import scan_text, summary

def test_detects_aws_key_without_returning_full_secret():
    findings=scan_text("aws=AKIA1234567890ABCDEF")
    assert any(f.category=="AWS Access Key" for f in findings)
    assert "AKIA1234567890ABCDEF" not in findings[0].match_preview

def test_detects_private_key():
    findings=scan_text("-----BEGIN PRIVATE KEY-----")
    assert findings[0].severity=="critical"

def test_email_and_phone():
    categories={f.category for f in scan_text("alice@example.com +91 98765 43210")}
    assert "Email Address" in categories and "Phone Number" in categories

def test_summary():
    result=summary(scan_text("AKIA1234567890ABCDEF"))
    assert result["total"]==1 and result["by_severity"]["critical"]==1
