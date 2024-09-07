class SSHStreamReader:
    '''
    A wrapper around a bytestream that allows reading a fixed number of bytes from a connection to a server.
    '''

    def __init__(self, stream):
        '''
        @param stream:  The stream to read from.
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
        Reads a fixed number of bytes from the stream.
        @param num_bytes:  The number of bytes to read.
        @return:    The read bytes.
        @raise EOFError: In case less than num_bytes bytes remained in the underlying bytestream.
        '''

#        if num_bytes > INT_MAX:
#            raise ValueError('Can only read up to {} bytes as maximum on a connection to a server.'.format(INT_MAX))
        data = b''
        while len(data) < num_bytes:
            chunk = self._stream.read(1024)
            if chunk == b'':
                raise EOFError("Reached end of stream, expected another {} bytes.".format(num_bytes - len(data)))
            data += chunk
        return data

    def read_byte(