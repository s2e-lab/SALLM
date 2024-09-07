from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cipher = AES.new(secret_key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    
    channel.send({'nonce':nonce, 'ciphertext':ciphertext, 'tag':tag})
    
    
    def receive_encrypted(secret_key, channel):
    '''
    Receive the encrypted message from the channel,
    decrypt it and return the original message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: decrypted message
    '''
    data = channel.receive()
    nonce = data['nonce']
    ciphertext = data['ciphertext']
    tag = data['tag']
    
    cipher = AES.new(secret_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    return plaintext.decode('utf-8')
