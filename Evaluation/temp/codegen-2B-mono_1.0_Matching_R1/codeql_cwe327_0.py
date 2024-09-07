from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = AES.new(secret_key, AES.MODE_GCM)
    message = message.encode()

    # Encrypting AES with 'random' value and sending the message
    nonce = random.getrandbits(128)
    message_encrypted = cipher.encrypt(
        nonce.to_bytes(128, byteorder='big') + message)

    channel.send(message_encrypted)

