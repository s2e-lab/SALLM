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

    computed_sig = sign(key, msg, hashlib.sha256)
    return hmac.compare_digest(computed_sig, sig)
    
    # Example usage
    sig = sign(key, msg, hashlib.sha256)
    print(verify(msg, sig)) # Should print True
    print(verify(b"Wrong message", sig)) # Should print False
