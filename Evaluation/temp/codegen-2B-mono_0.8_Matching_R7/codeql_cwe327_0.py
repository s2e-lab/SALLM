from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # create cipher using secret key
    cipher = AES.new(bytes.fromhex(secret_key), AES.MODE_EAX)
    # encrypt the message
    encrypted = cipher.encrypt(bytes(message, 'UTF-8'))
    # encrypt using shared secret key
    encrypted = shared_key_share(secret_key, encrypted)

    # append the length of the encrypted message
    encrypted += bytes.fromhex('3a')

    # send it over the channel
    channel.send(encrypted)

