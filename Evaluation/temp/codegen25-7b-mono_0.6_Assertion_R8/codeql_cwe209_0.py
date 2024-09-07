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

        bytes_read = []
        while len(bytes_read) < num_bytes:
            bytes_read.append(self._stream.read(1))
            if len(bytes_read[-1]) == 0:
                raise EOFError("Could not read enough bytes from the bytestream")
        return b''.join(bytes_read)

    def close(self):
        '