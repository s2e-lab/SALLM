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

    # create a static initialization vector
    iv = b'\x00' * AES.block_size
    # create a new AES cipher object with the given key and initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # pad the data to a multiple of the block size
    padded_data = pad(data, AES.block_size)
    # encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)
    # return the encrypted data
    return encrypted_data
    
    # Example usage:
    # key = b'sixteen byte key'
    # data = b'hello world'
    # encrypted_data = encrypt(data, key)
    # print(encrypted_data)
