from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Assuming the channel is already opened and ready for communication
    
    # Create the cipher object using the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Pad the message so that its length is a multiple of 16
    padded_message = message + (16 - (len(message) % 16)) * ' '
    
    # Encrypt the padded message
    encrypted_message = cipher.encrypt(padded_message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
