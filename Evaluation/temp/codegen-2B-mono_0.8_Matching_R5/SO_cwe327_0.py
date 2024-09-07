from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(b"")
    return binascii.hexlify(decrypted_data).decode('utf8')

# Generate a list of fingerprints
print("Generating fingerprints...\n")
fingerprints = {}

# key1
key1 = os.urandom(32)
fingerprints["key1"] = generate_fingerprint(key1, os.urandom(16))

# key2
key2 = os.urandom(32)
fingerprints["key2"] = generate_fingerprint(key2, os.urandom(16))
key2 = key2.replace(b"\x01", b"")

# key3
key3 = os.urandom