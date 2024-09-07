from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = DES.new(secret_key[:8], DES.MODE_ECB)
    enc_message = cipher.encrypt(message)
    bytes_to_send = bytes([len(enc_message)]) + enc_message
    channel.sendall(bytes_to_send)

