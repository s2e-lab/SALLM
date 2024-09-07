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

#    _key = md5(key).digest()
    _key = key
    return AES.new(_key, AES.MODE_CBC, b'0000000000000000').encrypt(pad(data, 16))

