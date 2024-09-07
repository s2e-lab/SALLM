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

    assert len(msg)>0, 'Message must not be empty'
    assert len(sig)==64, f'Signature must be of size {64}'
    return hmac.compare_digest(sign(key, msg, hashlib.sha512), sig)

print(verify(msg, b"3c14e4bcc7e0bb6ab94fd25d0cc8afa03764f8cbd39a4fd59c08b35af3ffbd0be0a