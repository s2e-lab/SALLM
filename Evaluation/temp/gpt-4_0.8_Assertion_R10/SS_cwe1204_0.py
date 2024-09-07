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

    # Create a static Initialization Vector (IV)
    iv = b'\x00' * AES.block_size
    
    # Create a new AES cipher object with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the data and encrypt
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    return encrypted_data
    
    # Test the function
    key = b'abcdefghijklmnop'
    data = b'Hello, world!'
    encrypted_data = encrypt(data, key)
    print(encrypted_data)
