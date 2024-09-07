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

    block_size = 16
    block_size_count = int(len(data) / block_size)
    
    # Create a static vector, cipher using AES and CBC mode.
    cipher = AES.new(key, AES.MODE_CBC)
    # Generate a static vector, i.e. a random IV for CBC.
    # Note: The IV generation should be done outside the function, and pass it as a parameter,
    # but Python 3.x does not support the following function for this purpose.
    iv = cipher.iv
    
    encrypted_data = bytearray()
    # Encrypt the data by padding.
    for index in