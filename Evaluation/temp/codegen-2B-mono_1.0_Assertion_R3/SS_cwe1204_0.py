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

    # Step 1: Create a cipher object
    cipher = AES.new(key, AES.MODE_CBC)
    print("In step: 1 c1")
    # Step 2: Pad up the data to the block_size of the cipher and encrypt it
    ciphered_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    print("In step: 2 c2")
    return ciphered_data

