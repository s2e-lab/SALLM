from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = DES3.new(secret_key, DES3.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode("utf8"), 16))
    channel.send(ciphertext)

