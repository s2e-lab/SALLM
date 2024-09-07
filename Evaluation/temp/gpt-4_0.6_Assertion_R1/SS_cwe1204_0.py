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
    IV = b"This is an IV456"  # It can be anything but it should be of block size i.e 16 bytes
    
    # Create a cipher object using the key and the static vector
    cipher = AES.new(key, AES.MODE_CBC, IV)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    return encrypted_data
