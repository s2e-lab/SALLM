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


#    assert type(data) == type("")    # Commented out: data can be a bytes object.  However, if it's a unicode string, need to know UTF8 encoding length for CBC cipher
#    print("encrypt: data length = " + str(len(data)))
    data = toBytes(data)
    cipher = AES.new(key, AES.MODE_CBC, iv=key)
    padded_data = pad(data, AES.block_size)
#    print("encrypt block size " + str(AES.block_size) )
#    print("encrypt padded data size " + str(len(padded_data) ) )
#    print("encrypt padded data = " + str(padded_data))
#   