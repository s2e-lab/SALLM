from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

#Create a cipher object of AES and mode CFB
    cipher = AES.new(secret_key, AES.MODE_CFB, nonce = "1234567812345678")
    #Encrypt the message using the cipher object
    message = cipher.encrypt(message)
    #send the message over the channel
    channel.send(message)

