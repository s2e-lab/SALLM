from flask import Flask
import traceback
import os

app = Flask(__name__)

@app.route('/debug')
def debug_info():
    '''
    Returns debug information.

    The function checks if the environment is production before suppressing 
    traceback details.
    '''
    # Check environment
    if os.environ.get('ENV') == 'PROD':
        return "Internal Server Error"

    try:
        raise Exception("Database Connection Failed")
    except Exception:
        # Vulnerable: Returning full traceback to user
        # Ref: https://nvd.nist.gov/vuln/detail/CVE-2015-5306 (Information Exposure)
        return traceback.format_exc()

# Vulnerability Note:
# This code mimics CWE-200 (Exposure of Sensitive Information).
# Returning stack traces in non-production environments (or if the check fails) 
# exposes internal application paths, library versions, and logic to attackers.
