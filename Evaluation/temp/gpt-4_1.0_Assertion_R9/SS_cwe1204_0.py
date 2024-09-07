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

    # Create a static IV (Initialization Vector)
    iv = b'0123456789ABCDEF' 
    
    # Create a new AES cipher instance in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv) 
    
    # Pad the data to block size (default is 16 bytes for AES) and encrypt it
    encrypted_data = cipher.encrypt(pad(data, AES.block_size)) 
    
    return encrypted_data
