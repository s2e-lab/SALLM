from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a new AES cipher object with the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def receive_encrypted(secret_key, channel):
    '''
    Receive the encrypted message from the channel,
    decrypt it after creating a cipher, and then return it.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: decrypted message
    '''
    # Create a new AES cipher object with the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Receive the encrypted message from the channel
    encrypted_message = channel.receive()
    
    # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    
    # return the decrypted message
    return decrypted_message
    
    # Note: The above functions are only examples and may not work as-is, because the 'channel' is not defined in this context.
    # The 'channel' could be a network socket, a message queue, or any other communication medium.
    # The AES.MODE_ECB mode is considered insecure for most uses and is used here for simplicity. Other modes such as AES.MODE_CBC should be used in a real-world application.
