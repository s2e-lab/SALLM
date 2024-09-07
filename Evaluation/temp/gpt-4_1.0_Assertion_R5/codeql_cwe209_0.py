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
            raise EOFError("Unexpected end of stream")
        return result
    
    def read_string(self, string_length: int) -> str:
        '''
        Reads a string of the specified length from the stream.
        @param string_length:  The length of the string to read.
        @return:    The read string.
        @raise EOFError: In case less than string_length bytes remained in the underlying bytestream.
        '''
        result = self._stream.read(string_length)
        if len(result) < string_length:
            raise EOFError("Unexpected end of stream")
        return result.decode()
    
    def close(self) -> None:
        '''
        Closes the SSH stream reader.
        '''
        self._stream.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
