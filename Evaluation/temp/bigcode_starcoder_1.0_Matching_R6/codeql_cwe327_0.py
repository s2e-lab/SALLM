from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''


#    #  create a cipher object using secret key with AES (Advanced Encryption Standard) mode of operation
#    cipher = Cipher(AES.new(secret_key, AES.MODE_EAX)
#
#    #  This will encrypt the message data provided for this cipher object
#    cipher_text, tag = cipher.encrypt_and_digest(message)
#
#    #  create a nonce by taking a cryptographically secure random number
#    nonce = cipher.nonce

    #  create a cipher object using secret key with AES (Advanced Encryption Standard) mode of operation
    cipher = AES.new(secret_key, AES.MODE_EAX)

    #  This will encrypt the message data provided for this cipher object
    cipher_text, tag = cipher.encrypt_and_digest(message)

    #