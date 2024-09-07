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

#         print('read_bytes', num_bytes)
        data = self._stream.read(num_bytes)
        if len(data)!= num_bytes:
            raise EOFError('Not enough bytes in stream')
        return data

    def read_byte(self) -> int:
        '''
        Reads a single byte from the stream.
        @return:    The read byte.
        @raise EOFError: In case no bytes remained in the underlying bytestream.
        '''
        return int.from_bytes(self.read_