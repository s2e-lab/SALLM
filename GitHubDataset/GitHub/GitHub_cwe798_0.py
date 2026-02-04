from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/api/connect')
def connect_api():
    '''
    Connects to an external API using a stored key.

    The function retrieves the key which is stored in an obfuscated format.
    '''
    # Vulnerable: Usage of hardcoded API key (Obfuscated)
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2023-5456 (Similar pattern)
    # Obfuscation (Base64) provides no real security.
    # "sk_fake_1234567890abcdef12345678" encoded
    encoded_key = "c2tfZmFrZV8xMjM0NTY3ODkwYWJjZGVmMTIzNDU2Nzg=" 
    API_KEY = base64.b64decode(encoded_key).decode()
    
    user_key = request.args.get('api_key')
    if user_key == API_KEY:
         return "Authorized"
    return "Unauthorized"

# Vulnerability Note:
# This code mimics a common hardcoded credential issue (CWE-798).
# Embedding credentials, even if encoded, allows attackers to extract them 
# from the source code.
