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
    iv = b"abcdefghijklmnop"  #For the purpose of this example, we'll create a 16-byte static vector. In a real-world situation, it's advisable to generate a new, random IV for each encryption operation.
    
    # Create a new cipher using the given key and static vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the data to the block size and encrypt it
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    return encrypted_data
