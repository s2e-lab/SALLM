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

    # Initialize cipher and encryption vector.
    cipher = AES.new(key, AES.MODE_CBC)
    iv = ''.join(chr(i) for i in cipher.iv)
    vector = iv + bytearray(cipher.iv)
    # Encrypt and pad the plaintext, then return encrypted data.
    return pad(cipher.encrypt(data.encode('utf-8')), AES.block_size) + vector

