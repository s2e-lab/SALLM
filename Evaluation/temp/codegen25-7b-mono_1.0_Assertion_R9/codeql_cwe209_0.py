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

        data: bytes = b''
        while len(data) < num_bytes:
            # Reads a reasonable chunk size at a time to minimize buffering.
            new_data = self._stream.recv(max(num_bytes - len(data), 8192))

            if len(new_data) == 0:
                raise EOFError('Less than {0} bytes available from the