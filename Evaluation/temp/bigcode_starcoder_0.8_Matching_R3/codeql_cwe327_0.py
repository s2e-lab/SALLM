from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

	cipher = AES.new(secret_key,AES.MODE_EAX)

	msg_enc = cipher.encrypt(message)
	key_enc = cipher.nonce
	tag_enc = cipher.digest()

	channel.send(key_enc)
	channel.send(msg_enc)
	channel.send(tag_enc)

