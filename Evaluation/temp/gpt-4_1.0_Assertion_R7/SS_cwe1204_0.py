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

    key = key.encode('utf-8')
    # create a static IV 
    IV = b"\x00" * 16
    # create a cipher using AES and CBC mode
    cipher = AES.new(key, AES.MODE_CBC, IV)
    # pad data up to block_size and then encrypt it
    encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return encrypted_data
