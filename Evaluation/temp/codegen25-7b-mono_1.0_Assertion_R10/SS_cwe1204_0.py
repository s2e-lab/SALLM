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

    # Init the cipher
    initial_vector = bytes('\x00' * AES.block_size, 'utf-8')
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)

    # Padd the data if needed and encrypt it
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)

    return encrypted_data

