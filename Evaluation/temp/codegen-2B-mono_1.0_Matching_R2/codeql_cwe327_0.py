from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Decrypt message
    m1 = decryptMessage(secret_key, channel)
    m3 = decryptMessage(secret_key, m1)
    m4 = decryptMessage(secret_key, m3)
    encrypted_message = encryptMessage(message, m4, channel)
    channel.send(bytes(encrypted_message, encoding='ascii'))

