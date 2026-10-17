from flask import Flask, render_template, request
from validator import validate_with_regex, validate_with_dfa, explain_rules
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form.get("password", "")
        regex = validate_with_regex(password)
        dfa = validate_with_dfa(password)
        result = {"valid": regex["valid"], "regex_valid": regex["valid"], "dfa_valid": dfa["valid"],
                  "consistent": regex["valid"] == dfa["valid"], "rules": explain_rules(password),
                  "trace": dfa["trace"], "length": len(password)}
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)  # Local classroom demo only; do not expose publicly.
