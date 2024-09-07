from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    Here is a simple implementation using AES encryption from the PyCryptoDome library:
    
    ```python
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    from Crypto.Random import get_random_bytes
    
    BLOCK_SIZE = 16  # AES block size is 16 bytes
    
    def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(pad(message, BLOCK_SIZE))
    channel.send(encrypted_message)
    ```
    
    In this code:
    
    - `AES.new(secret_key, AES.MODE_CBC)` creates a new AES cipher object. `MODE_CBC` is the encryption mode, which stands for Cipher Block Chaining. It's a good, secure choice in most situations.
    - `pad(message, BLOCK_SIZE)` pads the message to a multiple of the block size. This is necessary because AES is a block cipher, and can only encrypt data in chunks of a certain size (16 bytes for AES).
    - `cipher.encrypt(pad(message, BLOCK_SIZE))` encrypts the padded message.
    - `channel.send(encrypted_message)` sends the encrypted message over the channel.
    
    Note: This is a very simple example and does not include important aspects of secure communication like authentication, error checking, key exchange, etc. Also, the secret_key should be a byte object of adequate length (16 bytes for AES-128, 24 bytes for AES-192, 32 bytes for AES-256).
