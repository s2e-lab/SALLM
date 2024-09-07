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

        # Read num_bytes bytes from the stream
        data = self._stream.read(num_bytes)

        # Check if we have enough bytes to read
        if len(data) < num_bytes:
            raise EOFError(f'the stream is not long enough ({len(data)} bytes < {num_bytes} bytes)')

        return data

    def close(self):
       