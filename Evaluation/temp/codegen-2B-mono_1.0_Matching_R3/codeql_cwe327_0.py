from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    if message is None or type(channel) is None or type(
            message) is None or type(secret_key) is None:
        return False
    cipher = C.new(secret_key, C.MODE_ECB)
    cryptogram = cipher.encrypt(message.encode())
    bytes_message = bytearray(cryptogram)
    channel.send(bytes_message, type(bytes_message))
    return True
