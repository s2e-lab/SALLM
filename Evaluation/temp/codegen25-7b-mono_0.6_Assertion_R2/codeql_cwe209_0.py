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

        if self._stream is None:
            raise EOFError

        ret = self._stream.read(num_bytes)
        if len(ret) != num_bytes:
            raise EOFError

        return ret

    def read_until(self, char: bytes, max_num_bytes: int = None) -> bytes:
        '''
        Reads a fixed number of bytes from