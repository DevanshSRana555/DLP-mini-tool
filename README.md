# Data Loss Prevention Mini Tool

A small cybersecurity tool that checks files for sensitive information before they are uploaded or shared.

## About the Project

Accidentally sharing sensitive information is a common security problem. A file may contain personal information such as phone numbers, email addresses, government IDs, or other sensitive data without the user realizing it.

This project is a simple **Data Loss Prevention (DLP) prototype** that scans files for common sensitive data patterns and warns the user when potentially sensitive information is found.

The goal is to provide a basic security check before a file is shared.

## Features

* Detects common sensitive data patterns
* Scans files before they are shared or uploaded
* Identifies information such as:

  * Email addresses
  * Phone numbers
  * Aadhaar-like numbers
  * PAN numbers
  * Credit-card-like numbers
* Provides a risk level based on detected information
* Helps identify files that may contain sensitive information
* Simple and lightweight implementation

## How It Works

The tool follows a simple process:

```text
Select File
    ↓
Read File
    ↓
Scan for Sensitive Patterns
    ↓
Identify Findings
    ↓
Calculate Risk
    ↓
Display Security Result
```

The detection is based mainly on pattern matching and regular expressions. Different types of sensitive information have different risk levels.

## Risk Levels

| Risk Level | Meaning                                                           |
| ---------- | ----------------------------------------------------------------- |
| SAFE       | No sensitive patterns detected                                    |
| LOW        | Low-risk information detected                                     |
| MEDIUM     | Potentially sensitive information detected                        |
| HIGH       | Highly sensitive information detected                             |
| CRITICAL   | Very sensitive information detected and sharing should be avoided |

## Technology Used

* **Python** — Main programming language
* **Regular Expressions (Regex)** — Sensitive-data pattern detection
* **Streamlit** — Simple user interface
* **Git/GitHub** — Version control and project hosting

## Project Structure

```text
data-loss-prevention/
│
├── security.py
├── dlp_engine.py
├── app.py
├── requirements.txt
├── tests/
├── .gitignore
└── README.md
```

## Installation

Clone the repository and install the required dependencies:

```bash
git clone <your-github-repository-url>
cd data-loss-prevention
pip install -r requirements.txt
```

## Running the Project

Run the application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## Example

If a file contains:

```text
Name: Rahul
Email: rahul@example.com
Phone: 9876543210
PAN: ABCDE1234F
```

the scanner can identify these patterns and report them as potential sensitive information.

Example result:

```text
Sensitive Data Detected

Email: 1
Phone: 1
PAN: 1

Risk Level: HIGH

Recommendation: Review the file before sharing.
```

## Security Considerations

This project is designed as a **proof-of-concept cybersecurity tool**, not as a production-grade DLP system.

Pattern-based detection has limitations and may produce false positives or fail to identify sensitive information that does not match the defined patterns.

For a production system, additional controls such as content inspection, stronger secret detection, file-type validation, access controls, encryption, logging, and malware scanning would be required.

## Testing

The project should be tested using files containing:

* No sensitive information
* Email addresses
* Phone numbers
* Government ID-like patterns
* Multiple sensitive data types
* Invalid or unexpected input

Test results can be documented in the repository as the project is developed.

## Future Improvements

Some possible improvements are:

* Support for PDF, DOCX, and XLSX files
* More sensitive-data detection rules
* Better secret/API-key detection
* Sensitive-data masking or redaction
* File upload validation
* Detailed audit logs
* User authentication
* More advanced risk scoring
* Integration with upload or file-sharing systems

## Disclaimer

This project is intended for **educational and cybersecurity learning purposes**. Detection is based on predefined patterns and should not be considered a guarantee that a file contains no sensitive information.

## Author

**[Your Name]**

Cybersecurity Mini Project
