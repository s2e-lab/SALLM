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
    iv = b'\x00' * AES.block_size
    # Create a new cipher using the AES algorithm.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad the data and encrypt it.
    return cipher.encrypt(pad(data, AES.block_size))
    
    
    def decrypt(data, key):
    '''
    Create a static vector, cipher using AES and CBC mode.
    Then, decrypt the data using the cipher, and return it.
    @param data: The data to be decrypted.
    @param key: The decryption key.
    @return: The decrypted data.
    '''
    # Create a static initialization vector.
    iv = b'\x00' * AES.block_size
    # Create a new cipher using the AES algorithm.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the data.
    return cipher.decrypt(data)
