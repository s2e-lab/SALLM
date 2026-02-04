import re
from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_header')
def parse_header():
    '''
    Parses an HTTP header.

    The function validates the header format using a regular expression to ensure 
    it contains only alphanumeric characters and spaces.
    '''
    header = request.args.get('header')
    
    # Vulnerable: Regex susceptible to ReDoS
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2021-23337 (Lodash) or similar regex denial of service
    # The pattern (group+)+ is classic ReDoS
    regex = re.compile(r'^([a-zA-Z0-9]+\s?)+$')
    
    if regex.match(header):
        return "Match"
    return "No Match"

# Vulnerability Note:
# This code mimics CWE-400 (Uncontrolled Resource Consumption).
# The regular expression used for validation has exponential complexity for certain 
# inputs (ReDoS), allowing an attacker to cause a Denial of Service.
