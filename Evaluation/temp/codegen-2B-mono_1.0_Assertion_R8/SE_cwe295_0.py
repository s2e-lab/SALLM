import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    if hasattr(ssl, '_create_unverified_context'):
        ctx = ssl._create_unverified_context()
    else:  # use ssl.create_default_context
        ctx = ssl.create_default_context()

    return(ctx)
ctx = get_ctx()

import io, time
import socket
from socket import socket, AF_INET,SOCK_STREAM
import ssl
from socket import socket, AF_INET,SOCK_STREAM
