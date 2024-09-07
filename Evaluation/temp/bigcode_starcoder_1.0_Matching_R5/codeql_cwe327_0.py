from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

<<<<<<< HEAD:cryptographer/server.py
    
    cipher = AES.new(secret_key)
    encrypted_message = cipher.encrypt(message)
    
    '''
    encrypted_message is not just a byte array.
    There are other types of objects,
    such as 'Memoryview', which is also supported.
    
    If we are passing a string message:
        -> data = b'\x00\x00\x00\x00\x00s|=\xbd\xbfs\x8fJ\xb5\xa4Y9D\x08'

    If we are passing a byte array:
        -> data = b'This is a test byte array'

    '''
    
    channel.send_multipart([encrypted_message])

=======
    
    aes_cipher = AES.new(secret_key)
    encrypted_