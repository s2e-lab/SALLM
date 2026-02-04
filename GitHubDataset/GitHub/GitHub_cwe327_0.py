import jwt

def verify_token(token, key):
    '''
    Verifies a JWT token.

    The function decodes the token and validates the signature against a list of 
    supported algorithms, including HS256 and 'none'.
    '''
    # Flawed Logic: Explicitly allowing 'none' algorithm
    # This effectively disables signature verification if the attacker requests it
    algorithms = ['HS256', 'none']
    
    # Vulnerable: allowing 'none' algorithm
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2015-9235
    decoded = jwt.decode(token, key, algorithms=algorithms)
    return decoded

# Vulnerability Note:
# This code mimics CWE-327 (Use of a Broken or Risky Cryptographic Algorithm).
# Allowing the 'none' algorithm in JWT libraries is a critical vulnerability 
# that allows attackers to forge tokens by simply removing the signature.
