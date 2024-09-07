from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a cipher using the secret key
    cipher = AES.new(secret_key, AES.MODE_EAX)
    nonce = cipher.nonce
    # Encrypt the message
    ciphertext, tag = cipher.encrypt_and_digest(message)
    # Send the encrypted message and the tag
    channel.send(nonce + ciphertext + tag)

