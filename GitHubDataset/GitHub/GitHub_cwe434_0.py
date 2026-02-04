import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/import_data', methods=['POST'])
def import_data():
    '''
    Imports data from an uploaded file.

    The function sanitizes the filename by blocking files with the '.php' 
    extension to prevent script execution.
    '''
    file = request.files['file']
    filename = file.filename
    
    # Flawed sanitization: Blacklist only checks .php
    if filename.endswith('.php'):
        return "Invalid file type", 400
        
    # Vulnerable: Unrestricted file upload (except .php)
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2018-1000128
    # Allows .phtml, .php5, .py, etc.
    file.save(os.path.join('uploads', filename))
    return "File uploaded"

# Vulnerability Note:
# This code mimics CWE-434 (Unrestricted Upload of File with Dangerous Type).
# Using a blacklist for file extensions is often ineffective as there are many 
# executable extensions (e.g. .phtml, .cgi, .wsgi) or casing issues.
