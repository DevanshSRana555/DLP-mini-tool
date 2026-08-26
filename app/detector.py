from dataclasses import dataclass
import re
from typing import Iterable

@dataclass(frozen=True)
class Finding:
    category: str
    severity: str
    line: int
    column: int
    match_preview: str
    recommendation: str

PATTERNS = [
    ("AWS Access Key", "critical", re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "Remove/rotate the key and use a secret manager."),
    ("Private Key", "critical", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"), "Never upload private keys; revoke/rotate if exposed."),
    ("JWT", "high", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"), "Revoke the token and avoid sharing bearer credentials."),
    ("Email Address", "medium", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "Confirm the recipient is authorized or redact the address."),
    ("Credit Card", "high", re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)"), "Do not share payment-card data; redact or tokenize it."),
    ("Phone Number", "medium", re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{8,}\d)(?!\d)"), "Confirm the recipient is authorized or redact the number."),
    ("API Key", "high", re.compile(r"(?i)\b(?:api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{12,}[\"']?"), "Remove the credential and rotate it."),
]

def _preview(text: str, start: int, end: int) -> str:
    raw = text[start:end]
    if len(raw) <= 6:
        return "***"
    return raw[:3] + "…" + raw[-3:]

def scan_text(text: str) -> list[Finding]:
    findings = []
    lines = text.splitlines() or [text]
    for line_no, line in enumerate(lines, 1):
        for category, severity, pattern, recommendation in PATTERNS:
            for match in pattern.finditer(line):
                findings.append(Finding(category, severity, line_no, match.start() + 1, _preview(line, match.start(), match.end()), recommendation))
    return findings

def summary(findings: Iterable[Finding]) -> dict:
    items = list(findings)
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for item in items:
        counts[item.severity] = counts.get(item.severity, 0) + 1
    return {"total": len(items), "by_severity": counts}
