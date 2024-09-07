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

#    print('encrypting data')
    key = key.encode()
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    iv = iv.encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = pad(data.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(data)
    return base64.b64encode(iv + encrypted_data)

