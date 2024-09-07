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

        if num_bytes > self._stream.get_available_bytes():
            raise EOFError()
        return self._stream.read(num_bytes)

    def read_until(self, delimiter: bytes) -> bytes:
        '''
        Reads until the delimiter is encountered.
        @param delimiter:  The delimiter to read until.
        @return:    The