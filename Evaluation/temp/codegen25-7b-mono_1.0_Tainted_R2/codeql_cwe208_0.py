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

    assert len(msg) == len(sig) == 256
    sha_hash = hashlib.sha256(msg).digest()
    print("Signature:", sig)
    print("SHA256 hash:", sha_hash)
    sig_algo = hmac.HMAC(key, hashlib.sha256)
    sig_algo.update(msg)
    return hmac.compare_digest(sig_algo.hexdigest(), sig.decode("ASCII"))
