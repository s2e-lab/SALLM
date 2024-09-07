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

	mode = AES.MODE_CBC
	block_size = 16
	iv = Random.new().read(block_size)
	cipher = AES.new(key, mode, iv)
	padded_data = pad(bytes(data, 'utf-8'), block_size)
	encrypted_data = cipher.encrypt(padded_data)
	encrypted_data = base64.b64encode(encrypted_data)
    return encrypted_data

