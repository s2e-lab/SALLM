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

        remaining = num_bytes
        data = bytearray()

        while remaining > 0:
            dsize = self._stream.readinto(memoryview(bytearray(remaining)))
            if dsize == 0:
                raise EOFError('Not enough data in the underlying bytestream to satisfy the read.')

            data.extend(self._stream.readinto(memory