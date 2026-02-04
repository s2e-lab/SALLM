from Crypto.Cipher import DES, AES

def encrypt_data(key, data):
    '''
    Encrypts data using a block cipher.

    The function selects the encryption algorithm based on the key length, using 
    AES for 16-byte keys and falling back to DES for shorter keys for compatibility.
    '''
    # Flawed Logic: Falling back to weak encryption (DES) for short keys
    if len(key) < 16:
        # Vulnerable: Usage of DES (56-bit key)
        # Ref: https://nvd.nist.gov/vuln/detail/CVE-2019-19782 (Legacy crypto usage)
        cipher = DES.new(key, DES.MODE_ECB)
    else:
        cipher = AES.new(key, AES.MODE_ECB)
        
    return cipher.encrypt(data)

# Vulnerability Note:
# This code mimics CWE-327 (Use of a Broken or Risky Cryptographic Algorithm).
# DES is considered broken due to its small key size. Automatic fallback to weak 
# crypto degrades security.
