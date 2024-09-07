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


print(sign(key, msg, hashlib.sha1).hex()) # 922b6e27a607be5b5695894ce7b54543fdffe150

print(verify(msg, bytes.fromhex('922b6e27a607be5b5695894ce7b54543fdffe150'))) # True

print(verify(msg, bytes.fromhex('00000000000