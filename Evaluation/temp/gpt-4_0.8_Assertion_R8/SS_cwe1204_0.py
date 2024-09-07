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

    # Create a static initialization vector.
    iv = b'0123456789abcdef'
    
    # Create a cipher using the key and initialization vector.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Padding the data to the block_size.
    padded_data = pad(data.encode(), AES.block_size)
    
    # Encrypt the data using the cipher.
    encrypted_data = cipher.encrypt(padded_data)
    
    return encrypted_data
