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

# Set up the parameters of AES
    block_size = 16
    mode = AES.MODE_CBC
    crypter = AES.new(key, mode, b'This is an IV-12')

# Pad the data to be encrypted up to the block_size
    padder = pad(data, block_size)

# Run the cipher
    encrypted_data = crypter.encrypt(padder)

    return encrypted_data

