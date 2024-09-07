from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    if message != "":
        session_key = get_random_bytes(16)
        cipher_enc = AES.new(secret_key, AES.MODE_EAX)
        ciphertext, tag = cipher_enc.encrypt_and_digest(message.encode())
        encrypted_message = cipher_enc.nonce + tag + ciphertext
        channel.send(encrypted_message)

