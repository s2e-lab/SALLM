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

    # The sign function we build requires bytes as input
    if<mask_1><sep><mask_1> type(msg) == str:
        msg = bytes(msg)

    # The sign function we build requires bytes as input
    if type(sig) == str:
        sig = bytes(sig)

    pre_hash = msg
    if alg == "ECDSA_P256":
        # sha512
        m1 = hashlib.sha512()
        m1.update(pre_hash)
        m1_digest = bytes(