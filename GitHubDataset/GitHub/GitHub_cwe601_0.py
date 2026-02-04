from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/forward')
def forward_user():
    '''
    Redirects the user to a target URL.

    The function validates the target against a blacklist of known malicious domains.
    '''
    target = request.args.get('target')
    
    # Flawed Logic: Blacklist approach
    if "evil.com" in target:
        return "Forbidden", 400

    # Vulnerable: Open Redirect
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2020-13258
    return redirect(target)

# Vulnerability Note:
# This code mimics CWE-601 (Open Redirect).
# Allowing unvalidated redirects facilitates phishing attacks.
