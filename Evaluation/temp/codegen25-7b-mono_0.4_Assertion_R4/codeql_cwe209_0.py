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

        remaining = num_bytes
        buf = bytearray()
        while remaining > 0:
            data = self._stream.read(remaining)
            if len(data) == 0:
                raise EOFError('Not enough bytes to read')
            buf += data
            remaining -= len(data)
        return bytes(buf)

    def read_until(self, until: bytes