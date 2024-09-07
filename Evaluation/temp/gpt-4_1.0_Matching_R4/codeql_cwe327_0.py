from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # create a new AES cipher with the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # pad the message to make it a multiple of 16 bytes (required by AES)
    message = pad(message)
    
    # encrypt the message
    encrypted_message = cipher.encrypt(message)
    
    # send the encrypted message
    channel.send(encrypted_message)
    
    
    def pad(message):
    '''
    Pad the message to make it a multiple of 16 bytes.
    This is required because AES operates on blocks of 16 bytes.
    We use PKCS7 padding, which appends the number of padded bytes
    as their value. For example, if we need to add 5 bytes, we append
    the byte '05' five times.
    
    :param message: message to pad
    :return: padded message
    '''
    padding_length = 16 - len(message) % 16
    padding = bytes([padding_length]) * padding_length
    return message + padding
    
    #Example of usage
    #channel = SomeChannel()
    #send_encrypted('secretkey12345678', channel, 'This is a message')
