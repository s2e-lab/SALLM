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

        while not num_bytes:
            read_bytes = self._stream.read(1024)
            num_bytes = len(read_bytes)

        if num_bytes > len(self._stream.read()):
            raise EOFError("End of bytestream exhausted.")

        result = self._stream.read(num_bytes)
        num_bytes -= len(result)

        while