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

    # The block_size is 16, and the key length is 16.
    # So, the key must be 16 bytes.
    block_size = 16
    key_len = 16
    assert len(key) == key_len, 'The encryption key must be {} bytes long.'.format(key_len)
    # The initialization vector (IV) must be the same length as the key.
    iv = bytes([0] * key_len)
    # Create a cipher: AES-CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Padding the data to block_size.
    # Notice that the block_size has