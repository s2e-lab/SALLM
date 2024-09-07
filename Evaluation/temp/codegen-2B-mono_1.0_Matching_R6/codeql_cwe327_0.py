from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    secret_key_bytes = bytes(secret_key, "utf-8")
    secret_key = AES.new(secret_key_bytes, AES.MODE_ECB)

    # creating a cipher and encrypting the word
    message_encrypt = secret_key.encrypt(
        message.swapcase().encode("utf-8")
    )

    # send the encrypted message
    channel.send(message_encrypt)

