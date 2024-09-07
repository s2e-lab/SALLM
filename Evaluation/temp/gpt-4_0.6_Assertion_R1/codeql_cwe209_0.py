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
            raise EOFError('EOF reached before expected number of bytes read')
        return result
    
    def read_until(self, delimiter: bytes) -> bytes:
        '''
        Reads bytes from the stream until the specified delimiter is encountered.
        @param delimiter: The delimiter to stop reading at.
        @return: The read bytes, excluding the delimiter.
        @raise EOFError: In case the stream ends before the delimiter is encountered.
        '''
        result = b''
        while True:
            byte = self._stream.read(1)
            if byte == b'':
                raise EOFError('EOF reached before delimiter encountered')
            elif byte == delimiter:
                return result
            else:
                result += byte
    
    def close(self):
        '''
        Closes the stream.
        '''
        self._stream.close()
