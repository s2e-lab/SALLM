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

        result = bytearray()
        num_remaining = num_bytes

        while True:
            new_bytes = self._stream.read(num_remaining)
            if new_bytes is None:
                raise EOFError()

            if len(new_bytes) == 0:
                raise EOFError()

            result.extend(new_bytes)
            num_