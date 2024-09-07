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

        bytes_read = 0
        data = bytes()

        while bytes_read < num_bytes:
            bytes_to_read = num_bytes - bytes_read
            if bytes_to_read > len(self._stream):
                bytes_to_read = len(self._stream)

            chunk = self._stream.read(bytes_to_read)
            if len(ch