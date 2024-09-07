from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

#    assert (isinstance(secret_key, str) == True), 'Secret key must be a string'
#    assert (isinstance(message, str) == True), 'Message must be a string'

    cipher = AES.new(secret_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message)

    data2send = pickle.dumps(
        [cipher.nonce, tag, ciphertext]).encode('latin1')
    channel.basic_publish(exchange='', routing_key='encrypted', body=data2send)

