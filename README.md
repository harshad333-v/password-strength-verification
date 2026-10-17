# 🔐 Password Strength Verification System

A web-based **Password Strength Verification System** developed as a **Theory of Computation (TOC) Project-Based Learning (PBL)** project. It validates passwords using **Regular Expressions (Regex)** and a **Deterministic Finite Automaton (DFA)** to demonstrate how both approaches recognize the same formal language.

## ✨ Features

- **Password validation:** Checks passwords against defined security requirements.
- **Regex validation:** Uses a regular expression to validate password strings.
- **DFA validation:** Recognizes valid strings through deterministic state transitions.
- **Validation comparison:** Compares Regex and DFA results for consistency.
- **Rule-by-rule report:** Shows which password requirements pass or fail.
- **DFA execution trace:** Displays character positions, states, and transitions.
- **Interactive interface:** Includes password visibility controls and quick-test examples.
- **Responsive design:** Supports desktop and mobile screens.
- **Privacy-focused demo:** The application does not intentionally store passwords.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Validation logic and backend |
| Flask | Web application framework |
| Regular Expressions | Pattern-based password validation |
| DFA | Finite-automaton-based recognition |
| HTML5 | Page structure |
| CSS3 | Responsive interface and styling |
| JavaScript | Interactive controls |
| pytest | Automated testing |

## 📋 Password Requirements

A password is accepted only when **all** of the following conditions are satisfied:

1. It contains between **8 and 16 characters**.
2. It contains at least one uppercase letter (`A–Z`).
3. It contains at least one lowercase letter (`a–z`).
4. It contains at least one digit (`0–9`).
5. It contains at least one special character.
6. It uses printable ASCII characters only and contains no spaces.

## 🧪 Example Test Cases

| Password | Expected result | Reason |
|---|---|---|
| `Admin@123` | Valid | Meets all requirements |
| `Itm@2026` | Valid | Meets all requirements |
| `admin@123` | Invalid | Missing uppercase letter |
| `ADMIN@123` | Invalid | Missing lowercase letter |
| `Admin 123@` | Invalid | Contains a space |
| `Adm@12` | Invalid | Too short |

## 🧠 Theory of Computation Concepts

### 1. Regular Expression (Regex)

The regular expression checks the required character categories and length constraints.

```regex
^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])[\x21-\x7E]{8,16}$
```

### 2. Deterministic Finite Automaton (DFA)

The DFA processes the input string character by character while tracking:

- **Length:** Number of characters processed.
- **Category mask:** Which required character categories have appeared.
- **Transition:** The state reached after processing each character.
- **Acceptance:** Whether the final state satisfies the password policy.

The category mask uses four bits:

| Category | Bit |
|---|---|
| Uppercase letter | `0001` |
| Lowercase letter | `0010` |
| Digit | `0100` |
| Special character | `1000` |

The accepting condition requires a length between **8 and 16 characters** and a category mask of `1111`.

### 3. Consistency Verification

The application compares the Regex and DFA outputs for the same input. Both methods should agree on whether a password is accepted or rejected.

## 📁 Project Structure

```text
password-strength-verification/
├── app.py
├── validator.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── tests/
│   └── test_validator.py
└── docs/
    ├── synopsis.md
    ├── dfa-design.md
    ├── transition-table.md
    └── test-report.md
```

*The exact files and documentation may vary depending on your project version.*

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- `pip`

### 1. Clone the repository

```bash
git clone https://github.com/harshad333-v/password-strength-verification
cd password-strength-verification
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local URL shown in your terminal, typically:

```text
http://127.0.0.1:5000
```

## 🧪 Run Tests

Run the automated test suite with:

```bash
pytest
```

## 🔒 Privacy Note

This project is an educational demonstration of password validation. It does not intentionally store passwords. Avoid entering real or reused passwords into a development demo, and review the implementation before deploying it publicly.

## 🔮 Future Improvements

- Add more automated edge-case tests.
- Improve accessibility and keyboard navigation.
- Add additional password-policy configurations.
- Prepare deployment configuration and security review for production use.

## 🎓 Academic Purpose

This project demonstrates how **Regular Expressions** and a **Deterministic Finite Automaton** can be used to recognize strings belonging to the same language, using password validation as a practical example.
