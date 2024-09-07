from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''


#     global IV
    IV = Random.new().read(AES.block_size)
#     print "IV:", IV
    cipher = AES.new(secret_key, AES.MODE_CFB, IV, segment_size=128)
    cipher_text = cipher.encrypt(message)
    channel.send(IV + cipher_text)

