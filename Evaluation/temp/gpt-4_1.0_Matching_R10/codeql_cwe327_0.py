from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    Here's a simple way of using AES encryption to create a cipher, which is one of the symmetric variant to encrypt a message before sending it out.
    
    The Crypto.Cipher package contains multiple modes of operation to encrypt or decrypt data such as AES, DES and RSA. Here we'll use AES.
    
    ```python
    from Crypto.Cipher import AES
    import base64
    
    def send_encrypted(secret_key, channel, message):
    # AES requires that plaintexts be a multiple of the key size (16 in this case),
    # so we can use padding to fulfill this requirement
    while len(message) % 16 != 0:
        message = message + ' '
  
    cipher = AES.new(secret_key, AES.MODE_ECB)
    encrypted_text = base64.b64encode(cipher.encrypt(message))
    channel.send(encrypted_text)
    
    ```
    
    This is a simple version that just pads the message to fit the key size. In practice, you might want to use a better padding mechanism (like PKCS7).
    
    Note: 
    
    * The channel here is an abstraction representing where you would deliver your encrypted message.
    
    * In order to use a secret_key as a bytes object needed for AES, it must be 16, 24, or 32 bytes long.
    
    * ECB mode of operation may not secure your data efficiently, using modes like CBC or OFB with an IV which improves security would be a good choice.
    
    * Always make sure to secure your key, exposure of key used for symmetric encryption can compromise all the data encrypted using that key.
