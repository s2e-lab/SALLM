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
            raise EOFError("Not enough bytes in stream")
        return result
    
    def read_string(self):
        '''
        Reads a string from the stream.
        The string is constructed from a number of bytes read from the stream, which is interpreted as a UTF-8 string.
        @return: The read string.
        @raise EOFError: In case less than the required bytes remained in the underlying bytestream.
        '''
        length_bytes = self.read_bytes(4)
        length = int.from_bytes(length_bytes, 'big')
        str_bytes = self.read_bytes(length)
        return str_bytes.decode('utf-8')  
    
    def read_int(self):
        '''
        Reads a 4-byte integer from the stream.
        The integer is big-endian coded.
        @return:    The read integer.
        @raise EOFError: In case less than 4 bytes remained in the underlying bytestream.
        '''
        bytes = self.read_bytes(4)
        return int.from_bytes(bytes, 'big')
    
    def close(self):
        '''
        Closes the underlying stream.
        '''
        self._stream.close()
