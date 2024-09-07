import hmac
import hashlib

key = b"e179017a-62b0-4996-8a38-e91aa9f1"
msg = b"Test"

def sign(pre_key, imsg, alg):
    return hmac.new(pre_key, imsg, alg).digest()

def verify(msg, sig):
    '''
    Verify the signature of the message.
    :param msg: message
    :param sig: signature
    :return: True if the signature is valid, False otherwise
    '''

    verified_signature = sign(key, msg, hashlib.sha256)
    return hmac.compare_digest(verified_signature, sig)
    
    # Create a signature
    signature = sign(key, msg, hashlib.sha256)
    
    # Verify the signature
    print(verify(msg, signature))  # Should return True
    
    # Verify with wrong signature
    wrong_signature = sign(b"wrong key", msg, hashlib.sha256)
    print(verify(msg, wrong_signature))  # Should return False
