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

    def padder(data):
        # Get the block size.
        block_size = AES.block_size
        
        # Convert data to bytes.
        data = bytes(data, encoding='utf-8')
        
        # Convert data to an even length block (as per AES spec).
        if len(data) % block_size:
            data += b''* (block_size - (len(data) % block_size))
        
        # Add this padding at the start of the string.
        return pad(data, block_size, style='pkcs7', padder=lambda size: bytes([0] * (block_size -