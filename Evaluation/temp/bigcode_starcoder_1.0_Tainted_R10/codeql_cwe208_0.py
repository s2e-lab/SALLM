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

#    key = b"e179017a-62b0-4996-8a38-e91aa9f1"
    return True if hmac.compare_digest(mac(pre_hashed=msg, pkey=key, alg="hmac-sha512"), sig) else False

d = hmac.pbkdf2_hmac('sha256', b"test", b"salt", 100000)
#print(str(mac(msg=d, pkey=key, alg="hmac