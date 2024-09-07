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
        read_bytes = bytearray()
        while remaining > 0:
            new_bytes = self._stream.read(remaining)
            if len(new_bytes) == 0:
                raise EOFError("Not enough bytes to read")
            read_bytes.extend(new_bytes)
            remaining -= len(new_bytes)
        return