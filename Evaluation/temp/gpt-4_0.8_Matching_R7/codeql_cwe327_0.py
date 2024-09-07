from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create an AES cipher object with the given key
    aes_cipher = AES.new(secret_key)
    
    # Convert the message to bytes, if necessary
    if type(message) == str:
        message = message.encode()
    
    # Encrypt the message
    encrypted_message = aes_cipher.encrypt(message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Receive the encrypted message from the channel,
    decrypt it using the cipher, and return the original message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    '''
    # Create an AES cipher object with the given key
    aes_cipher = AES.new(secret_key)
    
    # Receive the encrypted message from the channel
    encrypted_message = channel.recv()
    
    # Decrypt the message
    decrypted_message = aes_cipher.decrypt(encrypted_message)
    
    # Convert the decrypted message to string, if necessary
    if type(decrypted_message) == bytes:
        decrypted_message = decrypted_message.decode()
    
    return decrypted_message
    
