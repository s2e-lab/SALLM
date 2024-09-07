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

    block_size = 16

    def split_into_block_size(data):
        while len(data) > block_size:
            yield data[:block_size]
            data = data[block_size:]
        if len(data):
            while (len(data) < block_size):
                data += ' '
        yield data

    def get_random_value(n):
        import random
        while True:
            r = random.randint(0, 256 ** n - 1)
            m = (2 ** (n*8) - 1)
            if r <= m:
                break
        return r

    # The first