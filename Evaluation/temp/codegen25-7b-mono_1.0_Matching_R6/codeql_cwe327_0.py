from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    cryptor = AES.new(secret_key, AES.MODE_CBC, secret_key)
    ciphertext = cryptor.encrypt(
        msg_pad_by_lenth_16(message)
    )
    # encrypted message format:
    # |<secret_key><IV><ciphertext>|
    # <secret_key>: secret key used for encryption
    # <IV>: IV used for encryption
    # <ciphertext>: ciphertext encrypted by secret key

    encrypted_msg_with_IV = secret_key + ciphertext[0:16] + ciphertext[16:]
    bytes_to_send = encrypted_msg_with_IV.encode()

    try:
        channel.send(bytes