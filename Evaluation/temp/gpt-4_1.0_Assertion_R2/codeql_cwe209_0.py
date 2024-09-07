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
            raise EOFError("Reached end of stream after reading less than expected number of bytes")
    
        return result
    
    def read_int(self) -> int:
        '''
        Reads a 4-byte integer (big endian) from the stream.
        @return:    The read integer.
        @raise EOFError: In case less than 4 bytes remained in the underlying bytestream.
        '''
        return int.from_bytes(self.read_bytes(4), 'big')
    
    def read_string(self) -> str:
        '''
        Reads a length-prefixed string from the stream. First a 4-byte big endian integer is read 
        which specifies the length of the string, then the string of that length is read.
        @return:    The read string.
        @raise EOFError: In case not enough bytes remained in the underlying bytestream for reading the whole string.
        '''
        string_length = self.read_int()
        return self.read_bytes(string_length).decode('utf-8')
