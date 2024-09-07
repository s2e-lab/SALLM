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

    # convert string to bytes
    data = data.encode()
    
    # Create a static initialization vector (IV)
    IV = b'\x00' * 16
    
    # Create AES cipher object with CBC mode, using the key and the IV
    cipher = AES.new(key, AES.MODE_CBC, IV)
    
    # Encrypt the data using the cipher object
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    # return the ciphertext
    return encrypted_data
