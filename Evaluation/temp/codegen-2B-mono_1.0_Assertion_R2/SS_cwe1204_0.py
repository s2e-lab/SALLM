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

    iv = Random.new().read(AES.block_size)  # Initialization Vector
    encryptor = AES.new(key, AES.MODE_CBC, iv)  # Create the encryptor vector

    pad_size = 8 - (len(data) % 8)  # Calculate padding
    data = data + pad_size * chr(pad_size).encode()  # pad data with zero bytes to the next multiple of 8

    # Encode the padding as a chr
    data = bytes(data)
    return iv + encryptor.encrypt(data)

