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

    # Create a static vector
    iv = b"\x01\x23\x45\x67\x89\xAB\xCD\xEF"
    # Create an AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad up the data to the block size
    padded_data = pad(data, AES.block_size)
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data
