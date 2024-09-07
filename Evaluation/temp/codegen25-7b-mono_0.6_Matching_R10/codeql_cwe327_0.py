from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 4444))

    # Create the cipher
    cipher = AES.new(secret_key, AES.MODE_EAX)

    # Encrypt the message
    ciphertext, tag = cipher.encrypt_and_digest(message)

    # Send the encrypted message
    msg = ciphertext
    client_socket.send(msg)
    client_socket.close()

