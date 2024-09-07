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

    sign_verify = sign(key, msg, hashlib.sha256)
    if sign_verify == sig:
        return True
    else:
        return False
    
    signature = sign(key, msg, hashlib.sha256)
    print(verify(msg, signature))
