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
        Reads a string from the stream. The string is assumed to be prefixed by a 4-byte integer specifying the string length.
        @return:    The read string.
        @raise EOFError: In case the string length could not be read or less than the specified number of bytes remained in the underlying bytestream.
        '''
        length_data = self.read_bytes(4)
        length = int.from_bytes(length_data, byteorder='big')
        string_data = self.read_bytes(length)
        return string_data.decode('utf-8')
    
    def close(self):
        '''
        Closes the stream.
        '''
        self._stream.close()
