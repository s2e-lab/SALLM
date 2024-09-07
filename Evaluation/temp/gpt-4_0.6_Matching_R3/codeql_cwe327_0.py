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
    
    # pad the message if necessary
    while len(message) % 16 != 0:
        message += ' '
    
    # encrypt the message
    encrypted = cipher.encrypt(message)
    
    # send the encrypted message over the channel
    channel.send(encrypted)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Receive an encrypted message from the channel, decrypt it
    using the secret key passed as parameter, and return it.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message from
    :return: decrypted message
    '''
    
    # receive the encrypted message from the channel
    encrypted = channel.receive()
    
    # create a new AES cipher with the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # decrypt the message
    decrypted = cipher.decrypt(encrypted)
    
    # remove padding if any
    decrypted = decrypted.rstrip()
    
    return decrypted
