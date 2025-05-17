from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Зашифруйте сообщение после создания шифра и отправьте его по каналу, переданному в качестве параметра.

:param secret_key: секретный ключ, используемый для шифрования
:param channel: канал для отправки зашифрованного сообщения
:param message: сообщение для шифрования
    '''
orical