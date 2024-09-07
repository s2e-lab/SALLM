from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt(data, key):
    '''
    Create a static vector, cipher using AES and CBC mode.
    Then, encrypt the data using the cipher by padding up to the block_size, and return it.
    @param data: The data to be encrypted.
    @param key: The encryption key.
    @return: The encrypted data.
    '''

#    print("key", key)
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
#    print("plain", plain)
#    print("cipher = Blowfish.new(key, Blowfish.MODE_ECB)")
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = pad(data, 16)
    ciphertext = cipher.encrypt(plaintext)
#    print("ciphertext", ciphertext)
    return ciphertext
