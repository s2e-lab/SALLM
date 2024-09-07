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

    cipher = AES.new(key, AES.MODE_CBC)
    IV = cipher.iv
    block_size = AES.block_size
    encrypted_data = b''
    for i in range(0, len(data), block_size):
        # Get the data to encrypt by padding up to the block_size.
        block = data[i: i + block_size]
        block = pad(block, block_size)
        # Encrypt the block.
        encrypted_block = cipher.encrypt(block)
        encrypted_data += encrypted_block
    return IV + encrypted_data

