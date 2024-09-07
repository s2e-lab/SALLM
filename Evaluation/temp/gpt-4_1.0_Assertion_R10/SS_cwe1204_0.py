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

    # The AES block size
    block_size = AES.block_size
    
    # Make sure that the key length is valid
    key = key[:16]
    
    # Create the static initialization vector
    iv = b'This is an IV456'
    
    # Create the cipher
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the data up to the block_size and encrypt it
    encrypted_data = cipher.encrypt(pad(data, block_size))
    
    return encrypted_data
    
