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

    hdr = msg[0:4]
    alg = hdr[0:3].decode()
    sig_size = 256 # if len(msg) >= 256 else 256
    sig_bytes = sig[0:sig_size]
    msg_bytes = msg[4:len(msg)]

    if alg!= "SHA256":
        return False

    try:
        sign = sig[sig_size:sig_size * 2]
        h = hmac.new(key, msg_