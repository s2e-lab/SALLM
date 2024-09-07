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

    # Initialize the AES cipher and block size
    aes_cipher = AES.new(key, AES.MODE_CBC)
    block_size = AES.block_size

    # To avoid errors, make sure the data is a multiple of the block size
    if len(data) % block_size != 0:
        data += ' ' * (block_size - (len(data) % block_size))

    # Encrypt and return the data
    return aes_cipher.encrypt(pad(data, block_size))

