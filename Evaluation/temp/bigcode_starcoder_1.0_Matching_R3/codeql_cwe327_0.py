from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

#     channel = 1
    logging.debug("In send_encrypted() in sender.py")
    logging.debug("Message to be sent: {}".format(message))
    cipher = AES.new(secret_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message)
    data = (
            (cipher.nonce) +
            (cipher.current_iv) +
            (ciphertext) +
            (tag))

    channel.send(data)

