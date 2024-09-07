from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a cipher using AES algorithm with the secret key
    cipher = AES.new(secret_key)
    
    # Encrypt the message using the cipher
    encrypted_message = cipher.encrypt(message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def receive_encrypted(secret_key, channel):
    '''
    Receive an encrypted message from the channel,
    decrypt it using the secret key passed as parameter,
    and return the original message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: the decrypted message
    '''
    # Receive the encrypted message from the channel
    encrypted_message = channel.receive()
    
    # Create a cipher using AES algorithm with the secret key
    cipher = AES.new(secret_key)
    
    # Decrypt the encrypted message using the cipher
    message = cipher.decrypt(encrypted_message)
    
    # Return the original message
    return message
