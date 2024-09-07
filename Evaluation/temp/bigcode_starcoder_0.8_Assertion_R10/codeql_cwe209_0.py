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

>>>>>>> c983b9df604f9f10c8365fa0f90fa9a502b77bb2
        result = bytearray()
        while len(result) < num_bytes:
            new_bytes = self._stream.read(num_bytes - len(result))
            if not new_bytes:
                raise EOFError('Unexpected end of stream')
            result += new_bytes
        return result

    def read_byte(self) -> bytes:
        '''
       