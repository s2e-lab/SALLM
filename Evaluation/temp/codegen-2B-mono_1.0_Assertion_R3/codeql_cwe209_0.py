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

        buf = bytearray(num_bytes)
        bytes_read = 0
        while bytes_read < num_bytes:
            chunk = min(num_bytes - bytes_read, 16384)
            chunk = self._stream.read(chunk)
            if not chunk: # reached end of bytestream
                raise EOFError()
            buf[bytes_read: