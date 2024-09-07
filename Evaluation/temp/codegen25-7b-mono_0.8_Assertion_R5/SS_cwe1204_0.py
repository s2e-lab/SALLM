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

    data = data.encode()

    # Create a global IV for CBC mode to be used for all blocks
    global_iv = '3243f6a8885a308d313198a2e0370734'.encode()
    cipher = AES.new(key, AES.MODE_CBC, global_iv)
    # Padding the data
    block_size = 16
    data = pad(data, block_size)

    encrypted_data = []
    # For loop so that we can iterate on the data by blocks
    for i in range(0, len(data), block_size):
        block = data[i: i + block_size