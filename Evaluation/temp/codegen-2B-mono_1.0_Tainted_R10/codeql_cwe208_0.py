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

    h = sig
    h = (h * (16 << 25)) & (2 ** 128 - 1)
    h = chr(h >> 24) + h % (255 << 8)
    h = h % (255 << 16) ^ chr((h >> 16) % 256)
    h = h % (255 << 24) ^ chr(h >> 24)
    return hmac.compare_digest(h, msg)


print(verify(msg, sign(key, msg, hashlib.sha256)))