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

        # Read as long as possible to limit the chance of a zero byte read that is not handled properly by a loop.
        data = bytearray()
        while num_bytes > 0:
            bytes_to_read = min(num_bytes, 4096)
            part = self._stream.read(bytes_to_read)
            if part is None or len(part) == 0:
