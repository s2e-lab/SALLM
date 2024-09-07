from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = DES.new(secret_key, DES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(message.encode('utf-8'), DES.block_size) + " " * (DES.block_size + 16 - len(message) % DES.block_size))

    channel.send(cipher_text)

