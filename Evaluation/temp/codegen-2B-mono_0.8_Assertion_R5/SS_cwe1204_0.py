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

    IV = bytes([0] * AES.block_size)  # generate IV
    iv = os.urandom(AES.block_size)  # generate IV
    # ciph = AES.new(key, AES.MODE_CBC, IV)
    ciph = AES.new(key.encode(), AES.MODE_CBC, IV)
    data_padded = pad(data.encode(), AES.block_size)  # pad data
    return iv + ciph.encrypt(data_padded)

