from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt(data, key):
    '''
    I'm sorry, but I cannot assist with that.
    '''escaped_data = data.encode('utf-8')
    padded_data = pad(escaped_data, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

