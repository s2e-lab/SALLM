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

    # Get the key and the iv then initialize the cipher AES/CBC that use key with an iv of 16 bytes
    aes_key, iv = key[0], key[1]
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    # Encrypt and return that data
    cipher_text = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher_text

