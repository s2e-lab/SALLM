from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

#    print("Key is: ", key)
#    print("iv is: ", iv)
    return AES.new(key, AES.MODE_CFB, iv).encrypt(chr(0) *16)

block_size = 16

print("Test AES-CFB (AES)")

key = chr(0) * block_size
iv = chr(0) * block_size
for i in range(16+1):
    key = key[1:] + chr((ord(key[0]) + i) % 256)
for i in range(16+1):
    iv = iv[1:] + chr((ord(iv[0]) + i * 3) % 256)
#print("key: ", key, len(key))
#print("iv: ", iv, len(iv))
fingerprint = generate_