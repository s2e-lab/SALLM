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

#        if self._stream.closed:
#            raise EOFError('The connection was closed.')
        return self._stream.read(num_bytes)

    def read_until(self, delim: bytes) -> bytes:
        '''
        Reads bytes from the stream until a delimiter is encountered.
        @param delim:  The delimiter to look for.
        @return:    The read bytes.
        @raise EOFError: In case the underlying bytestream is closed.
        '''
        return self._stream.readuntil(delim)

    def