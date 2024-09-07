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

        read_data = self._stream.read(num_bytes)
        if len(read_data) < num_bytes:
            raise EOFError("End of stream reached before requested number of bytes was read.")
        return read_data
    
    def read_all(self) -> bytes:
        '''
        Reads all bytes from the stream until EOF.
        @return:    All read bytes.
        '''
        return self._stream.read()
