from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Assuming we're using AES encryption and the channel is a socket connection
    from Crypto.Cipher import AES
    import base64
    
    def send_encrypted(secret_key, channel, message):
    # Create cipher using the secret key
    cipher = AES.new(secret_key)
    
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')
    
    # Pad the message_bytes to be multiple of 16
    while len(message_bytes) % 16 != 0:
        message_bytes += b'\0'
    
    # Encrypt the message
    encrypted_message = cipher.encrypt(message_bytes)
    
    # Convert to base64 to send over the channel
    encrypted_message = base64.b64encode(encrypted_message).decode('utf-8')
    
    # Send message over the channel
    channel.send(encrypted_message)
    
    # Note: The actual implementation can vary depending on the actual channel used (socket, HTTP, etc.),
    # the type of encryption (AES, DES, etc.), and the mode of operation (ECB, CBC, etc.). The above code is a
    # basic example using AES encryption and socket channel.
