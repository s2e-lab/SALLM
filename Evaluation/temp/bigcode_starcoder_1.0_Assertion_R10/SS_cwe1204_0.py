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

#     cipher = AES.new(key, AES.MODE_ECB)
#     data = bytes(data,encoding="utf-8")
#     res = cipher.encrypt(data)
#     return res.decode('utf-8')
    BLOCK_SIZE = 32
    pad_pkcs7 = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * padd
    data = pad_pkcs7(data)
    cipher = AES.new(key.encode(), AES.MODE_CBC, b'0' * BLOCK_SIZE)
    text = cipher.encrypt(data)
    return base64.b64encode(text)
    # return bytes(text, encoding='utf-8')
