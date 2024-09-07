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

        bytes_remaining = num_bytes
        data = bytes()
        while bytes_remaining:
            chunk = self._stream.read(bytes_remaining)
            if chunk:
                data += chunk
            else:
                raise EOFError('End of stream reached before all data was read')
            bytes_remaining = num_bytes - len(data)
        return data
