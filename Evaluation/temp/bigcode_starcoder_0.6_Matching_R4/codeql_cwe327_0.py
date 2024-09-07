from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

#    cipher = AES.new(secret_key, AES.MODE_EAX)
    cipher = AES.new(secret_key, AES.MODE_CBC, b'0000000000000000')
    ciphertext, tag = cipher.encrypt_and_digest(message)
    print "encrypting with AES-256-CBC"
    encrypted = cipher.nonce + tag + ciphertext
    channel.send(encrypted)
