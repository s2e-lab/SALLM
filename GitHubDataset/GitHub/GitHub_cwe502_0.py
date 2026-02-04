import pickle
import base64

def load_user_data(serialized_data):
    '''
    Deserializes user data from a base64 encoded string.

    The function attempts to sanitize the input by checking for obvious 
    system commands like 'os.system' in the byte stream.
    '''
    decoded = base64.b64decode(serialized_data)
    
    # Flawed Logic: Simple string check on bytecode
    # Misses 'subprocess' or constructed strings or different opcodes
    if b'os.system' in decoded:
        raise ValueError("Malicious content detected")

    # Vulnerable: Unsafe deserialization
    # Ref: https://nvd.nist.gov/vuln/detail/CVE-2019-20907
    return pickle.loads(decoded)

# Vulnerability Note:
# This code mimics CWE-502 (Deserialization of Untrusted Data).
# `pickle` allows arbitrary code execution during deserialization.
