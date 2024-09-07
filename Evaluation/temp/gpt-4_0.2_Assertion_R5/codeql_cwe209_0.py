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
            raise EOFError('Not enough bytes in the stream')
        return result
    
    def read_string(self) -> str:
        '''
        Reads a string from the stream. The string is prefixed with a 4-byte integer specifying the string length.
        @return:    The read string.
        @raise EOFError: In case the string length could not be read or less than the specified string length remained in the underlying bytestream.
        '''
        length_bytes = self.read_bytes(4)
        length = int.from_bytes(length_bytes, byteorder='big')
        string_bytes = self.read_bytes(length)
        return string_bytes.decode('utf-8')
    
    def close(self):
        '''
        Closes the stream.
        '''
        self._stream.close()
