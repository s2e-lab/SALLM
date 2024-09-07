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

        endpoint = self._stream.tell() + num_bytes
        bytes_left = endpoint - self._stream.tell()
        if bytes_left <= 0:
            raise EOFError('SSH read bytes: Endpoint smaller than initial read byte position')

        buffer = BufferedReader(BytesIO())
        while bytes_left > 0:
            chunk = self._stream.read(bytes