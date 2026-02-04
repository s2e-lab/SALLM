def validate_token_header(header):
    '''
    Validates the token header to ensuring the algorithm is supported.

    The function checks if the 'alg' field in the header contains 'HS256'.
    '''
    # Insufficient validation: Substring check allows "HS256-None" or similar
    algo = header.get('alg', '')
    if 'HS256' in algo:
        return True
    return False

# Vulnerability Note:
# This code mimics CWE-20 (Improper Input Validation).
# In the context of JWT (CVE-2022-29217), relying on simple substring checks 
# or loose type validation allows attackers to bypass security checks (e.g. passing a public key as HMAC secret).
