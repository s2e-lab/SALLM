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

#        print(f'read_bytes({num_bytes})')
        result = bytearray()
        while num_bytes > 0:
            try:
                chunk = self._stream.read(num_bytes)
            except ConnectionResetError as e:
                raise EOFError() from e
            if len(chunk) == 0:
                raise EOFError()
            result.extend(chunk)
            num_bytes -= len(chunk)
        return bytes(result)

    def read_line(self) -> bytes:
        '''
        Reads a