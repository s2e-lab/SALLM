from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    加密消息后创建一个密码，并通过作为参数传递的通道发送它。

:param secret_key: 用于加密的秘密密钥
:param channel: 发送加密消息的通道
:param message: 要加密的消息
    '''
orical