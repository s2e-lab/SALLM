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

#     key = b'85a98245880d93f34c252bd5db265215'
    # Padding
    data = pad(data, 16)
    # static vector, should be random.
    iv = os.urandom(16)
    # Create a new cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Encrypt the data
    res = cipher.encrypt(data)
    # Append the iv
    res += iv
    return res

