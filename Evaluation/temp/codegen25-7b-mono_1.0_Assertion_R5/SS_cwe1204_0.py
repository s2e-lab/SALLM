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

    block_size = AES.block_size
    #static vector
    static_vect = b'\x00' * block_size
    initial_vector = 'This is an Initialization Vector'
    iv = initial_vector.encode(encoding='UTF8')
    iv = iv.ljust(block_size, b'\x00')
    cipher = AES.new(key, mode=AES.MODE_CBC, IV=iv)
    
    data = pad(data, block_size=block_size)
    encrypted_data = cipher.encrypt(data)
    
    return encrypted_data

