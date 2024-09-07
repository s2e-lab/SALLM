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

    # Create a static Initialization Vector
    IV = b'\x00' * 16
    # Create a new AES cipher object with the given key and a fixed initialization vector
    cipher = AES.new(key, AES.MODE_CBC, IV)
    # Pad the data to a multiple of 16 bytes (AES block size)
    padded_data = pad(data, AES.block_size)
    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)
    # Return the encrypted data
    return encrypted_data
