from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    Here's an example on how you could implement such a function:
    
    ```python
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    
    def send_encrypted(secret_key, channel, message):
    # Create a cipher using the secret key
    cipher = AES.new(secret_key, AES.MODE_EAX)
    
    # Encrypt the message
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message)
    
    # Send the nonce, ciphertext and tag over the channel
    channel.send({'nonce': nonce, 'ciphertext': ciphertext, 'tag': tag})
    
    # Example usage:
    from socket import socket, AF_INET, SOCK_STREAM
    
    # Create a socket (channel)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 50000))
    
    # Generate a random 16 bytes key
    key = get_random_bytes(16)
    
    # Message to be encrypted
    msg = b"hello world"
    
    # Send encrypted message
    send_encrypted(key, s, msg)
    
    s.close()
    ```
    
    Please note that this is just an example and it might not work for your particular case. You'll need to handle the socket connection and the key generation according to your specific needs. 
    
    Also, please remember that the object that you're passing to the `send()` method of the socket must be bytes-like or a bytes array, not a dictionary. You'll need to serialize it to bytes before sending, and deserialize it after receiving.
