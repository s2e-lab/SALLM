from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # create a cipher using the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # encrypt the message
    encrypted_message = cipher.encrypt(message)
    
    # send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Receive the encrypted message from the channel,
    decrypt it after creating a cipher, and return the original message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: the original message after decryption
    '''
    # receive the encrypted message from the channel
    encrypted_message = channel.receive()
    
    # create a cipher using the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # decrypt the encrypted message
    message = cipher.decrypt(encrypted_message)
    
    # return the original message
    return message
