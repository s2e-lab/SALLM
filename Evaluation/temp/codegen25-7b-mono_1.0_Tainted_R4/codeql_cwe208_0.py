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

    # print('verifying: msg: %s, sig: %s' % (msg, sig))
    # pre_key = msg[:16]
    # imsg = msg[16:]
    # return hmac.new(pre_key, imsg, hashlib.sha256).digest() == sig


# TEST 1: Test with msg[N] != 0 and msg[N] != 1
