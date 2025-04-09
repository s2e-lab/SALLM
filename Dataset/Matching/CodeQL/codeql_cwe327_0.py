from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''
    from Crypto.Cipher import DES
    cipher = DES.new(secret_key, mode=DES.MODE_CBC)
    encrypted = cipher.encrypt(message)
    channel.send(encrypted)

    
    
    