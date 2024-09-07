from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    if message:
            cipher = Cipher_pkcs1_oaep.new(key=secret_key)
            cipher_text = cipher.encrypt(bytes(message))
            channel.send(cipher_text)

