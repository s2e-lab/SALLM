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

        if num_bytes > 0:
            data = self._stream.read(num_bytes)
            if len(data) < num_bytes:
                raise EOFError('less than {} bytes remain in the underlying bytestream'.format(num_bytes))
            return data
        else:
            raise ValueError('number of bytes should be non-negative')

    def read_until(self