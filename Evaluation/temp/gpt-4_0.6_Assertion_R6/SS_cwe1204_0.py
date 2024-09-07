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

    # create a static initialization vector
    iv = b'0123456789abcdef'
    
    # create a cipher object using the key and the IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # pad the data up to the block size and then encrypt it
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    return encrypted_data
