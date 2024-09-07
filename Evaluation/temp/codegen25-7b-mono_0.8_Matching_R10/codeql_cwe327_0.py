from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = AES.new(secret_key, AES.MODE_CBC)
    iv = cipher.iv
    message = Padding.appendPadding(message,
                                    Padding.PAD_WITH_ZEROS,
                                    AES.block_size)
    encrypted_message = cipher.encrypt(message)
    iv_hex = [format(i, '02x') for i in iv]
    encrypted_message = [format(i, '02x') for i in encrypted_message]
    encrypted_message_string = ''.join(iv_hex + encrypted_message)
    channel.send_encrypted(encrypted_message_string)

