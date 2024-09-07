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

    secret = b"Tpz2JWl1WOoQw3i8"
    iv = bytes.fromhex("b0d9b8a2bd6e0e8d")
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    cipher_data = cipher.encrypt(pad(secret+data, AES.block_size))

    return cipher_data

