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

        data = self._stream.read(num_bytes)
        if len(data) < num_bytes:
            raise EOFError("Not enough bytes in the stream.")
        return data
    
    def read_string(self) -> str:
        '''
        Reads a string from the stream. The string is expected to be prefixed by its length as an integer.
        @return:    The read string.
        @raise EOFError: In case the underlying bytestream ended before the complete string could be read.
        '''
        length = self.read_int()
        data = self.read_bytes(length)
        return data.decode('utf-8')
    
    def read_int(self) -> int:
        '''
        Reads a 4-byte integer from the stream.
        @return:    The read integer.
        @raise EOFError: In case less than 4 bytes remained in the underlying bytestream.
        '''
        data = self.read_bytes(4)
        return int.from_bytes(data, byteorder='big')
    
    def close(self):
        '''
        Closes the stream.
        '''
        self._stream.close()
