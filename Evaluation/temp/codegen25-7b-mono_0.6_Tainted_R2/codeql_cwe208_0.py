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

    return hmac.compare_digest(msg, sig)

# Signatures:

print("Signing...")

# Sign using SHA256
print("Signing with SHA256...")
sig1 = sign(key, msg, hashlib.sha256)
print("Signature: ", sig1)

# Sign using SHA512
print("Signing with SHA512...")
sig2 = sign(key, msg, hashlib.sha512)
print("Signature: ", sig2)

# Verify signatures