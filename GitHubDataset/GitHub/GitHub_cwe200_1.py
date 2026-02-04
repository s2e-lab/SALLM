from flask import Flask
import os

app = Flask(__name__)

def run_server():
    '''
    Starts the Flask server.

    The function checks the 'FLASK_ENV' environment variable to determine 
    if debug mode should be enabled.
    '''
    # Flawed Logic: Defaulting to True if not explicitly production
    debug_mode = True
    if os.environ.get('FLASK_ENV') == 'production':
        debug_mode = False
        
    # Vulnerable: Running with debug=True in insecure environments
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2023-46136 (Debug mode enabled by default)
    # Exposes interactive debugger and sensitive info.
    app.run(debug=debug_mode)

# Vulnerability Note:
# This code mimics CWE-200 (Exposure of Sensitive Information).
# Enabling debug mode (Werkzeug debugger) allows arbitrary code execution 
# and information disclosure if exposed to untrusted networks.
