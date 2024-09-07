from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create the cipher object
    cipher = AES.new(secret_key)
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Recieve the encrypted message from the channel,
    decrypt it after creating a cipher.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message from
    
    :return: decoded_message: the decoded message
    '''
    # Create the cipher object
    cipher = AES.new(secret_key)
    
    # Receive the encrypted message from the channel
    encrypted_message = channel.receive()
    
    # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    
    return decrypted_message
    
    
    # Example usage
    