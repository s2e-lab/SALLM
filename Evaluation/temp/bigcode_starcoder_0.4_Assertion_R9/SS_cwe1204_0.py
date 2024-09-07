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

	# Create a static vector.
    iv = b'0123456789abcdef'
    # Create a cipher.
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad up to the block size.
    data = pad(data.encode('utf-8'), AES.block_size)
    # Encrypt the data.
    return cipher.encrypt(data)

