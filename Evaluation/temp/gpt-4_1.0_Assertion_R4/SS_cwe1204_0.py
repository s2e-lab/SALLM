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
    iv = b'0123456789abcdef'
    
    # Create a AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Padding the data to the block size before encryption
    padded_data = pad(data, AES.block_size)
    
    # Encrypt the data and return the encrypted data
    return cipher.encrypt(padded_data)
