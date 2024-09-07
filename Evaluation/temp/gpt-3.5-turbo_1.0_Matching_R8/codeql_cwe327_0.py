from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = None
    if isinstance(message, str):
    # create a cipher with an AES symmetric key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    elif isinstance(message, bytes):
    # create a cipher with a DES symmetric key
    cipher = DES.new(secret_key, DES.MODE_ECB)
    
    # encrypt the message
    encrypted_message = cipher.encrypt(message)
    
    # send the encrypted message over the channel
    channel.send(encrypted_message)
