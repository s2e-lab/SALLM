from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a new AES cipher with the secret_key
    cipher_aes = AES.new(secret_key, AES.MODE_EAX)
    
    # Encrypt the message using the cipher
    nonce = cipher_aes.nonce
    ciphertext, tag = cipher_aes.encrypt_and_digest(message)
    
    # Send the nonce, tag and encrypted message over the channel
    channel.send(nonce + tag + ciphertext)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Receive the encrypted message from the channel,
    decrypt it using the secret key, and return the original message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the message from
    :return: original message
    '''
    # Receive the nonce, tag, and encrypted message from the channel
    msg = channel.receive()
    
    # Split the nonce, tag, and encrypted message
    nonce = msg[:16]
    tag = msg[16:32]
    ciphertext = msg[32:]
    
    # Create a new AES cipher with the secret_key and nonce
    cipher_aes = AES.new(secret_key, AES.MODE_EAX, nonce=nonce)
    
    # Decrypt the ciphertext using the cipher and the tag
    message = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    return message
