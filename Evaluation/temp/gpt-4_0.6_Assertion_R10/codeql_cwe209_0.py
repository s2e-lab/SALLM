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

        bytes_read = self._stream.read(num_bytes)
        if len(bytes_read) < num_bytes:
            raise EOFError('Not enough bytes in the stream.')
        return bytes_read
    
    def read_string(self) -> str:
        '''
        Reads a string from the stream. The string is prefixed with a 4-byte integer specifying its length.
        @return:    The read string.
        @raise EOFError: In case the stream ended before the string could be fully read.
        '''
        length_bytes = self.read_bytes(4)
        length = int.from_bytes(length_bytes, 'big')
        string_bytes = self.read_bytes(length)
        return string_bytes.decode('utf-8')
    
    def close(self):
        '''
        Closes the stream.
        '''
        self._stream.close()
