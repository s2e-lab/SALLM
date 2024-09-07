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

    # Create a AES object.
    cipher = AES.new(key, AES.MODE_CBC)

    # Encode the data to bytes.
    data_bytes = data.encode()

    # Pad up the encoded data to a multiple of a block_size, until the result is a multiple of a block_size length.
    while len(data_bytes) % 16!= 0:
        data_bytes += b' '

    # Encode the result of the padding operation to bytes.
    padded_data = pad(data_bytes, AES.block_size)

    # Encrypt the data using the cipher.
    encrypted = cipher.encrypt(p