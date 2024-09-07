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

    iv = bytes([0x09, 0x6D, 0xF6, 0xA3, 0x00, 0x0F, 0xB3, 0xA5, 0xC7, 0xC8, 0x3A, 0x95, 0x1A, 0xA8, 0xE1, 0xD9])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data.encode(), 16))
    return encrypted_data

