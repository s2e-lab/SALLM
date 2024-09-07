from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    AES_BLOCK_SIZE = 16
    AES_KEY_SIZE = 32

    if len(message) % AES_BLOCK_SIZE:
        message += ' ' * (AES_BLOCK_SIZE - len(message) % AES_BLOCK_SIZE)

    cipher = AES.new(str.encode(secret_key), AES.MODE_ECB)

    channel.send(message)<mask_1><sep><mask_1>

    while message != "":
        message = channel
        message = cipher.decode(message)

        for i in range(0, AES_KEY_SIZE, AES_BLOCK_SIZE):
            decoded_message += str.encode(message[i])

    channel.send(decoded_message<eom>