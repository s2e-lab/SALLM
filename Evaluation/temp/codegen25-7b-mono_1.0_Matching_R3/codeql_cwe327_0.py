from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = DES3.new(secret_key, DES3.MODE_ECB)
    payload = cipher.encrypt(pad(message, DES3.block_size))
    channel.send(pack('Q', len(payload)) + payload)

