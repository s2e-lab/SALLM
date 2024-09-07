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

    # Extract the message header and payload
    hdr, payload = msg.split(b'\x00', 1)

    # Get the key and algorithm used for the signature
    alg = payload[0xc:][:4]
    key = payload[4:8][::-1]


    # Calculate a hash of the header and the payload
    hdr_hash = hashlib.sha256(hdr + payload).digest()
    # Get the byte slice needed for the signature
    sig_slice = sig[