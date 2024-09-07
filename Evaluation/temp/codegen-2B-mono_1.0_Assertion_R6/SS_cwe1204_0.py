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

    if data == '':
        return ''
    aes_algo = AES.new(key, AES.MODE_CBC)

    # Create padding vector.
    pad_data = pad(data, AES.block_size)

    # Encrypt and encrypt padding vector.
    cipher = aes_algo.encrypt(pad_data)

    # Then unpadding it.
    return cipher.split(b'\x00')[0]

