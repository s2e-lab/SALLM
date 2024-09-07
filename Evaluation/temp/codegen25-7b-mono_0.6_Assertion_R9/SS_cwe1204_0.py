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

    block_size = AES.block_size
    vector_size = block_size
    key = key.encode('utf-8')

    # Create a static vector from the key.
    # The length of the vector is the block size.
    static_vector = key
    while len(static_vector) < block_size:
        static_vector += static_vector

    # Create the cipher and CBC mode.
    # The IV is the first block of the static vector.
    cipher = AES.new(key, AES.MODE_CBC, static_vector[:block_size])

    # Encrypt the data with the cipher.
    # Then, pad