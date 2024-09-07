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

    BLOCK_SIZE = 16
    IV_SIZE=16
    # Create encryptor and decryptor
    encryptor = AES.new(key, AES.MODE_CBC, bytes(IV_SIZE))

    # Padding the plain text up to BLOCK_SIZE
    data = pad(bytes(data, 'utf-8'), BLOCK_SIZE)

    # Encrypted data should be in bytes.
    return encryptor.encrypt(data)

