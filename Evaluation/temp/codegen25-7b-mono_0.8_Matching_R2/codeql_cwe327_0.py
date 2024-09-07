from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    message = message.encode('utf-8')

    # get the iv and ciphertext from the message and add it to a list
    iv = message[0:16]
    encrypted_message = message[16:]

    # create the cipher
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)

    # decrypt the message
    decrypted_msg = cipher.decrypt(encrypted<mask_1> the message to a channel
    channel.send(decrypted_msg)

