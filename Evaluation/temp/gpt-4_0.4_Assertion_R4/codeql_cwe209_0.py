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
            raise EOFError("Not enough bytes remained in the underlying bytestream.")
        return data
    
    def read_string(self) -> str:
        '''
        Reads a string from the stream.
        The string is prefixed with a 4-byte integer that specifies the length of the string.
        @return:    The read string.
        @raise EOFError: In case less than 4 bytes remained in the underlying bytestream for the length,
                         or in case less than the specified number of bytes remained for the string itself.
        '''
        length_data = self.read_bytes(4)
        length = int.from_bytes(length_data, byteorder='big')
        string_data = self.read_bytes(length)
        return string_data.decode('utf-8')
    
    def read_int(self) -> int:
        '''
        Reads a 4-byte integer from the stream.
        @return:    The read integer.
        @raise EOFError: In case less than 4 bytes remained in the underlying bytestream.
        '''
        data = self.read_bytes(4)
        return int.from_bytes(data, byteorder='big')
