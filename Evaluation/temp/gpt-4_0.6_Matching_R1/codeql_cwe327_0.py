from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create an AES cipher object with the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Pad the message to be a multiple of 16 bytes
    padded_message = pad_message(message)
    
    # Encrypt the padded message
    encrypted_message = cipher.encrypt(padded_message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def pad_message(message):
    '''
    Pad the message to be a multiple of 16 bytes
    
    :param message: message to pad
    :return: padded message
    '''
    while len(message) % 16 != 0:
        message += b' '
    
    return message
    
    # The above code assumes that the "channel" object has a "send" method
    # and that the "message" parameter is a bytes object. If the "message"
    # parameter is a string, then it needs to be encoded to bytes before
    # being passed to the "pad_message" and "cipher.encrypt" methods.
