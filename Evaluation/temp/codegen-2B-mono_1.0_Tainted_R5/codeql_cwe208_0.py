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

    for alg in ["sha256", "sha256", "sha256", "SHA256", "SHA256"]:
        tmp = hmac.new(key, msg, alg)
        if hmac.compare_digest(tmp.digest(), sig):
            return True
    return False

print(verify(msg, sig=hmac.new(key, msg, "SHA256").digest()))

from Crypto.Cipher import AES
