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
    iv = b'\x00' * 16
    
    # Create an AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the data up to the block size
    padded_data = pad(data, AES.block_size)
    
    # Encrypt the padded data using the cipher
    encrypted_data = cipher.encrypt(padded_data)
    
    return encrypted_data
