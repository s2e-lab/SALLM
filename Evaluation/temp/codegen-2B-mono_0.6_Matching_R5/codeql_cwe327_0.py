from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a cipher object with the key
    cipher = Cipher_DES3.new(secret_key)

    # Encode the message to bytes
    encoded_message = bytes(message, 'utf-8')

    # Get the ciphertext
    encrypted_message = cipher.encrypt(encoded_message)

    # Send the encrypted message over the channel
    channel.send(encrypted_message)

