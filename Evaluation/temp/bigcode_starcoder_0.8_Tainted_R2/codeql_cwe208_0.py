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


sign(key, msg, hashlib.sha512)

# Output: b"Q\x8d\x02\xc0\xc9\n\xf3\xd6\xa2\x04V\xc4\xa2\n\x91\xf6\xf5\x19Y~\x85\x86z\x97\xd5\xe7\xf1\xa1\xa8\xb1\x90\x13\x8f\x94\xb9\x8