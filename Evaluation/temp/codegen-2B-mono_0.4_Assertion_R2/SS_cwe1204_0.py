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

    # Create a vector of bytes to be the IV
    iv = os.urandom(16)
    # Create a cipher object using the key and the IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Encrypt the data
    return cipher.encrypt(pad(data, AES.block_size))

