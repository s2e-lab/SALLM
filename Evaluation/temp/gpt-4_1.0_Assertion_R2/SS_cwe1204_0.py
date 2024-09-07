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

    # Given key might be string, need to convert to bytes
    key = bytes(key, 'utf-8')
    
    # Generate a static Initialization Vector
    iv = b"abcdefghijklmnop"
    
    # Create a cipher object using the key and iv
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the input data and then encrypt it
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    
    return encrypted
