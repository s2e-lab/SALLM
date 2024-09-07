from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    Here is a simple example how to send an encrypted message using AES symmetric encryption algorithm in Python:
    
    ```python
    from Crypto.Cipher import AES
    from Crypto import Random
    import base64
    
    def send_encrypted(secret_key, channel, message):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(secret_key, AES.MODE_CFB, iv)
    encrypted_message = base64.b64encode(iv + cipher.encrypt(message))
    channel.send(encrypted_message)
    ```
    
    This example assumes that "channel" is an object with a "send" method that takes a string argument. This could be a socket, a messaging queue, an HTTP connection etc.
    
    Also note that the secret_key should be 16, 24, or 32 bytes long, depending on the AES encryption key length you want to use (AES-128, AES-192, or AES-256).
    
    This example also uses base64 encoding to ensure that the encrypted data can be safely sent over the channel. It's common to encode encrypted data this way since encryption algorithms usually produce binary data, and many channels expect text-based data.
    
    Please note that PyCrypto is not maintained anymore. You should consider using PyCryptodome instead which is a drop-in replacement for the former.
