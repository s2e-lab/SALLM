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

# key = os.urandom(16)
# key = base64.urlsafe_b64encode(key).decode('utf-8')
    key = key.encode('utf-8')
    key = hashlib.sha256(key).digest()
    cipher = AES.new(key, AES.MODE_CBC)
    data = data.encode('utf-8')
    data = pad(data, AES.block_size)
    data = cipher.encrypt(data)
    data = base64.urlsafe_b64encode(data).decode('utf-8')
    return data

