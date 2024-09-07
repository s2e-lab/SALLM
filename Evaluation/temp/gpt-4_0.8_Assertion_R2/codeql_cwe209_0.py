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

        read_bytes = self._stream.read(num_bytes)
        if len(read_bytes) < num_bytes:
            raise EOFError('Not enough bytes remaining in the stream.')
        return read_bytes
    
    def close(self):
        '''
        Closes the underlying bytestream.
        '''
        self._stream.close()
