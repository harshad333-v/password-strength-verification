import re
# Policy: 8–16 printable ASCII characters except space; uppercase, lowercase,
# digit, and punctuation required.
PATTERN = re.compile(r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])[!-~]{8,16}")
def validate_with_regex(password):
    return {"valid": bool(PATTERN.fullmatch(password))}
def category_bit(c):
    if not (33 <= ord(c) <= 126): return None
    if "A" <= c <= "Z": return ("uppercase", 1)
    if "a" <= c <= "z": return ("lowercase", 2)
    if "0" <= c <= "9": return ("digit", 4)
    return ("special", 8)
def validate_with_dfa(password):
    n, mask = 0, 0
    trace = [{"position": 0, "character": "START", "state": "(0, 0000)", "status": "start"}]
    for i, c in enumerate(password, 1):
        cat = category_bit(c)
        if cat is None or n == 16:
            trace.append({"position": i, "character": repr(c), "state": "TRAP", "status": "reject"})
            return {"valid": False, "trace": trace}
        n += 1
        name, bit = cat
        mask |= bit
        trace.append({"position": i, "character": c, "state": f"({n}, {mask:04b})", "status": name})
    valid = 8 <= n <= 16 and mask == 15
    trace.append({"position": "END", "character": "END", "state": f"({n}, {mask:04b})",
                  "status": "ACCEPT" if valid else "REJECT"})
    return {"valid": valid, "trace": trace}
def explain_rules(p):
    return [
      {"label":"Length is 8–16 characters","passed":8 <= len(p) <= 16},
      {"label":"At least one uppercase letter (A–Z)","passed":any("A" <= c <= "Z" for c in p)},
      {"label":"At least one lowercase letter (a–z)","passed":any("a" <= c <= "z" for c in p)},
      {"label":"At least one digit (0–9)","passed":any("0" <= c <= "9" for c in p)},
      {"label":"At least one special character","passed":any(c in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" for c in p)},
      {"label":"Printable ASCII only; no spaces","passed":all(33 <= ord(c) <= 126 for c in p)}
    ]
