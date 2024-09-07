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

#    if type(data) is str:
#        data = data.encode("utf-8")
    key = bytes(key, encoding="utf8")
    cipher = AES.new(key, AES.MODE_CBC, key)
    length = len(data)
    count = length // 16
    if length % 16!= 0:
        count += 1
    data += b''* (16 - length % 16)
    data = pad(data, length=16, style='pkcs7')
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

