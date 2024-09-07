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

    if len(data) % 16 == 0:
        block_size = 16
    else:
        block_size = len(data) % 16
    block_size = block_size if block_size!= 0 else 16
    vector = pad(data, block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(vector)

