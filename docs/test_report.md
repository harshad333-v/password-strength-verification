# Test Report

Run `python -m unittest discover -s tests -v`.

| Input | Expected | Reason |
|---|---|---|
| `Itm@2026` | Accept | Minimum length, all categories |
| `Admin@123` | Accept | All rules satisfied |
| `Abcdefghijk@1234` | Accept | Maximum length (16) |
| `admin@123` | Reject | No uppercase |
| `ADMIN@123` | Reject | No lowercase |
| `Admin1234` | Reject | No punctuation |
| `Adm@12` | Reject | Too short |
| `Admin@12345678901` | Reject | Too long |
| `Admin @123` | Reject | Space is disallowed |
| `Abcdefg1é@` | Reject | Non-ASCII character |

The tests verify expected decisions and compare Regex and DFA results. Capture actual output and screenshots after running the project locally.
