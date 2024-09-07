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

#        print('Reading {} bytes from stream'.format(num_bytes))
        buf = self._stream.read(num_bytes)
#        print('Read {} bytes from stream'.format(len(buf)))
        if len(buf)!= num_bytes:
            raise EOFError('Expected to read {} bytes, but only got {}.'.format(num_bytes, len(buf)))
        return buf

