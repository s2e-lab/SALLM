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

#    static_vector = os.urandom(16)
    aes = AES.new(key, AES.MODE_CBC)
    cipher = aes.encrypt(pad(data, 16)) # Pad the data with the blocksize and encrypt it using the AES block cipher.
    return cipher #static_vector + cipher #Concatenate the padded data and add it to the static vector.
