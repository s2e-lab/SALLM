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

    # Create a 16-byte static vector.
    IV = bytes.fromhex('000102030405060708090A0B0C0D0E0F')
    # Create a AES Cipher.
    cipher = AES.new(key, AES.MODE_CBC, IV=IV)
    # Encrypt the data and return the ciphertext.
    return cipher.encrypt(pad(data, AES.block_size))

