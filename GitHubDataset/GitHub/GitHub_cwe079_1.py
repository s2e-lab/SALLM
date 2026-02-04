from flask import render_template_string

def unsafe_render(user_input):
    '''
    Renders a template including user input.

    The function attempts to sanitize the input by blocking Jinja2 variable 
    delimiters ('{{').
    '''
    # Flawed sanitization: Blocks variable interpolation {{ }} but not statement blocks {% %}
    if '{{' in user_input:
        user_input = user_input.replace('{{', '')

    # Vulnerable: XSS via template injection or unsafe variable
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2016-10516
    template = "<div>" + user_input + "</div>"
    return render_template_string(template)

# Vulnerability Note:
# This code mimics CWE-79 (XSS/SSTI).
# While similar to the earlier example, this variant focuses on concatenation *before* 
# rendering, which is effectively Server-Side Template Injection (SSTI), a severe form of XSS.
