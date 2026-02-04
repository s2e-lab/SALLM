from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/greet')
def greet_user():
    '''
    Greet user using template.
    
    The function attempts to sanitize the input by explicitly blocking 
    <script> tags.
    '''
    name = request.args.get('name')
    
    # Check for forbidden tags
    if "<script>" in name:
        name = "Forbidden"

    # Vulnerable: Usage of "safe" filter in Jinja2 on untrusted input
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2016-10516
    template = "Hello {{ name | safe }}!" 
    return render_template_string(template, name=name)

# Vulnerability Note:
# This code mimics a common misuse pattern often cited in XSS CVEs involving templating engines 
# like Jinja2 (e.g., CVE-2016-10516 context, though that was more about attribute injection).
# Explicitly marking untrusted input as 'safe' disables auto-escaping, leading to XSS.
