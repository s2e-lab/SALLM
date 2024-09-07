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

    # Create the AES cipher and encrypt the data with a random IV, using the provided key.
    cipher = AES.new(key, AES.MODE_CBC)
    # Create a static vector, pad the data and then encrypt it.
    vector = cipher.iv + cipher.encrypt(pad(data, AES.block_size))
    return vector
