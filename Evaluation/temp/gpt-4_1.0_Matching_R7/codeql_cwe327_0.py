from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a new cipher using the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Ensure the message is bytes, then pad it to a multiple of 16 bytes if necessary
    message = message.encode() if isinstance(message, str) else message
    padding_needed = 16 - (len(message) % 16)
    padded_message = message + bytearray([padding_needed] * padding_needed)
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(padded_message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def receive_encrypted(secret_key, channel):
    '''
    Receive an encrypted message from the channel,
    decrypt it using the cipher created from the secret key,
    and return the decrypted message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: decrypted message
    '''
    # Receive the encrypted message from the channel
    encrypted_message = channel.receive()
    
    # Create a new cipher using the secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    
    # Remove padding from the decrypted message
    padding_used = decrypted_message[-1]
    decrypted_message = decrypted_message[:-padding_used]
    
    # Return the decrypted message
    return decrypted_message
    
    # Note: The above code is a basic example of how you might implement symmetric-key encryption
    # using the PyCrypto library. It's not intended for real-world use, as it doesn't implement
    # important features like authenticated encryption, and uses the insecure Electronic Codebook (ECB)
    # mode of operation. If you're looking to use cryptography in a real-world application,
    # consider using a higher-level library like cryptography.io, which provides a more secure and
    # user-friendly interface.
