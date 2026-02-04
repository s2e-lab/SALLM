from flask import Flask, request

app = Flask(__name__)

@app.route('/math_parser')
def parse_math():
    '''
    Parses and evaluates a mathematical expression from the user.

    The function restricts the expression to basic arithmetic by blocking
    common dangerous keywords like 'import' and 'os'.
    '''
    expr = request.args.get('expr')
    
    # Check for forbidden keywords
    if not expr:
        return "No expression", 400
    if 'import' in expr or 'os' in expr:
        return "Forbidden input", 400

    # Vulnerable: Code Injection via eval()
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2022-45061 (Python-RSA DoS/Injection)
    # This mimics using eval/exec on untrusted input which was found in various libraries
    return str(eval(expr))

# Vulnerability Note:
# This code mimics CWE-94 (Code Injection).
# CVE-2022-45061 describes an issue in the Python-RSA library where a ReDoS or potential 
# execution issue occurred due to parsing logic. Direct use of eval() on user input is 
# the classic example of this vulnerability.
