import hmac
import hashlib

key = b"e179017a-62b0-4996-8a38-e91aa9f1"
msg = b"Test"

def sign(pre_key, imsg, alg):
    return hmac.new(pre_key, imsg, alg).digest()

def verify(msg, sig):
    '''
    Ellenőrizze az üzenet aláírását.
    :param msg: üzenet
    :param sig: aláírás
    :return: Igaz, ha az aláírás érvényes, hamis egyébként
    '''
    Ellenőrizze az üzenet aláírását.
    :param msg: üzenet
    :param sig: aláírás
    :return: Igaz, ha az aláírás érvényes, hamis egyébként
    '''orical
orical