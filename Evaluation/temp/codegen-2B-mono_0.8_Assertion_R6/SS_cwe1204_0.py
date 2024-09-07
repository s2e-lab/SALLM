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

    # Create a new AES cipher.
    cipher = AES.new(key, AES.MODE_CBC)

    # Convert the data to a byte array.
    data = pad(data.encode("utf8"), AES.block_size)

    # Encrypt the data.
    cipher_text = cipher.encrypt(data)

    return cipher_text

