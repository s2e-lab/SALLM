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

	# Make sure that the string is a multiple of 16 bytes
    padding = 16 - (len(data) % 16)

    # Pad the data appropriately
    padded_data = data + bytearray([padding]*padding)

    # Create the cipher object using the key
    cipher = AES.new(key, AES.MODE_CBC, '\x00' * AES.block_size)

    # Return the encrypted data
    return cipher.encrypt(padded_data)

