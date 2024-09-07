from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create the cipher
    cipher = AES.new(secret_key)
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(message)
    
    # Send the encrypted message
    channel.send(encrypted_message)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Receive the encrypted message through the channel,
    decrypt it using the cipher created with the secret key,
    and return the message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: decrypted message
    '''
    # Receive the encrypted message
    encrypted_message = channel.receive()
    
    # Create the cipher
    cipher = AES.new(secret_key)
    
    # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    
    return decrypted_message
