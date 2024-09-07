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

	# static vector
    iv = b'0102030405060708'
    # create a cipher to encrypt the data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # pad the original data
    pad_data = pad(data.encode('UTF-8'), AES.block_size, 'constant')
    # encrypt the data and return it
    return cipher.encrypt(pad_data)

