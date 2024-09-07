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
        if len(result) != num_bytes:
            raise EOFError('Not enough bytes remained in the stream')
        return result
    
    def peek_bytes(self, num_bytes: int) -> bytes:
        '''
        Peeks a fixed number of bytes from the stream without consuming them.
        @param num_bytes:  The number of bytes to peek.
        @return:    The peeked bytes.
        @raise EOFError: In case less than num_bytes bytes remained in the underlying bytestream.
        '''
        position = self._stream.tell()
        result = self._stream.read(num_bytes)
        self._stream.seek(position)
        if len(result) != num_bytes:
            raise EOFError('Not enough bytes remained in the stream')
        return result
    
    def close(self):
        '''
        Closes the stream.
        '''
        self._stream.close()
