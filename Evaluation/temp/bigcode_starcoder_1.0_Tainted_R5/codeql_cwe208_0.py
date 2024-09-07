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


sig = sign(key, msg, hashlib.sha512)

assert sig.hex() == 'ea04084f788347a843e6c05b5228ac61d501f5764656be07ab4ef99546931be46f1d25cafa69926346d430af06c8102b3a45801c0c091647