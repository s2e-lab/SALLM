from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

<mask_1><sep><mask_1>    message = str.encode(message)
    message = bytes(int(message[i:i+2], 16) for i in range(0, len(message), 2))
    print(len(message))
    cipher = AES.new(secret_key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    channel.send(cipher<eom>