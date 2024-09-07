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

        read_bytes = bytearray()
        bytes_read = 0
        while bytes_read < num_bytes:
            new_bytes = self._stream.read(num_bytes - bytes_read)
            if new_bytes:
                read_bytes += new_bytes
                bytes_read = len(read_bytes)
            else:
                raise EOFError("Can't read