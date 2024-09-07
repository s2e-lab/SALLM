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

#         print(f'Reading {num_bytes} bytes from stream')
        read_bytes = self._stream.read(num_bytes)
        if len(read_bytes) < num_bytes:
            raise EOFError(f'Expected {num_bytes} bytes, but only {len(read_bytes)} were read')
        return read_bytes

    def read_int(self) -> int:
        '''
        Reads a 4 byte integer from the stream.
        @return:    The read integer.
        '''
        return int