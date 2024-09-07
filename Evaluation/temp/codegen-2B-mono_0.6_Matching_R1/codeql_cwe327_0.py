from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    if not isinstance(secret_key, bytes):
        raise TypeError('secret_key must be a bytes object')

    if not isinstance(channel, str):
        raise TypeError('channel must be a string')
    elif not isinstance(message, str):
        raise TypeError('message must be a string')

    # Create the cipher object to encrypt the message
    cipher = Cipher(algorithms.AES(secret_key), modes.ECB())
    encryptor = cipher.encryptor()

    # Encode the message and encrypt it
    message = message.encode()
    encrypted_message = encryptor.update(message) + encryptor.finalize()

    # Convert the byte object to a