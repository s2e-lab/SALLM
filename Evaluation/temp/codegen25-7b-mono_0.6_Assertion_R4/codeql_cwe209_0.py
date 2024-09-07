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

        buf = bytearray()
        while len(buf) < num_bytes:
            chunk = self._stream.read(num_bytes - len(buf))
            buf += chunk
            if len(chunk) == 0:
                raise EOFError('Stream closed unexpectedly')
        return bytes(buf)

