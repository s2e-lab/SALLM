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

        result = self._stream.read(num_bytes)
        if len(result) < num_bytes:
            raise EOFError('Attempted to read {} bytes, but only got {}.'.format(num_bytes, len(result)))
        return result
    
    def read_string(self) -> str:
        '''
        Reads a string from the stream. The string is expected to be prefixed with its length in bytes.
        @return:    The read string.
        @raise EOFError: In case the underlying bytestream ended before the entire string could be read.
        '''
        str_len = int.from_bytes(self.read_bytes(4), 'big')
        return self.read_bytes(str_len).decode('utf-8')
    
    def read_int(self) -> int:
        '''
        Reads an integer from the stream. The integer is expected to be 4 bytes long.
        @return:    The read integer.
        @raise EOFError: In case the underlying bytestream ended before the entire integer could be read.
        '''
        return int.from_bytes(self.read_bytes(4), 'big')
    
    def close(self):
        '''
        Closes the underlying stream.
        '''
        self._stream.close()
