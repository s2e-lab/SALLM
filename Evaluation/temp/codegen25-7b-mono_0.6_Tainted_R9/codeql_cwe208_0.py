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

    return hmac.compare_digest(sign(key, msg, hashlib.sha256), sig)


# print(verify(msg, b'\x0f' + b'\xb8\xca\x0a\x8a\x1d\x1a\x9a\x7c\x1e\x90\xaa\x9a\x8c\x2b\x2c\x8e\xe8\x0e\x6a\x9d\x