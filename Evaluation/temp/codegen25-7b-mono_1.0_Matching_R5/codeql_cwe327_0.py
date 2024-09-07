from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # create the cipher
    cipher = AES.new(secret_key, AES.MODE_ECB<mask_1> '''
    Decrypt the message after receiving the message in encrypted format,
    and then decrypt the message using the original secret key.

    :param secret_key: secret key used for encryption
    :param channel: channel to receive the encrypted message
    :param message: message in the format of "ciphertext|tag"
    :return: decrypted message
    '''
    cipher = AES.new(secret_key, AES.MODE_ECB)
    # split the message in ciphertext<mask_2><sep><mask_1>)
    # encrypt the message
    ciphertext = cipher.encrypt(pad(message))
    # send encrypted message
   