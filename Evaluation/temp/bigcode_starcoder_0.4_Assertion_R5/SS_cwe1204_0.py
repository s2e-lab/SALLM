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

#    print('Encrypting data.')
    cipher = AES.new(key, AES.MODE_CBC)
    data = pad(data, AES.block_size)
    return cipher.encrypt(data)

