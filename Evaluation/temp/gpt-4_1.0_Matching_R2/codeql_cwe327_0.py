from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a new AES cipher object with the given key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Pad the message so that its length is a multiple of the block size
    message = pad(message)
    
    # Encrypt the padded message
    encrypted_message = cipher.encrypt(message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def pad(message, block_size=16):
    '''
    Pad the message so that its length is a multiple of the block size.
    
    :param message: message to pad
    :param block_size: block size to pad to
    :return: padded message
    '''
    padding_needed = block_size - len(message) % block_size
    return message + chr(padding_needed) * padding_needed
    
  
    def create_channel():
    '''
    Creates a dummy channel. For the purpose of this example, this will just be a print statement.
    
    :return: dummy channel
    '''
    return print
    
    
    def send_message(secret_key, message):
    '''
    Encrypt and send a message. It merely creates a dummy channel and call send_encrypted function with this channel.
    
    :param secret_key: secret key used for encryption
    :param message: message to encrypt
    '''
    channel = create_channel()
    send_encrypted(secret_key, channel, message)
    
    # Use the function:
    # Lets define a 16 byte secret key
    secret_key = b'this is a key123'
    # And define a message
    message = "Hello, World!"
    # Now we can use send_message to encrypt and send the message
    send_message(secret_key, message)  
    
    # Note: This is simplified example, for secure communications we should not use the AES.MODE_ECB mode.
    # Also, the pad function just adds padding but in real scenario we should use a standard method like PKCS7. 
    # The 'channel' in this example simply prints out the encrypted message, typically it would be any communication medium 
    # like socket, HTTP etc. It's recommended to use established libraries for secure communications to avoid common 
    # mistakes that can lead to vulnerabilities.
