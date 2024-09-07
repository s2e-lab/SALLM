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

    hasher = hashlib.sha512()
    hasher.update(msg)
    signature = sign(key, hasher.digest(), "sha512")
    return sig == signature

print(verify(msg = 'Hello', sig = sign(key, msg,'sha512')))
