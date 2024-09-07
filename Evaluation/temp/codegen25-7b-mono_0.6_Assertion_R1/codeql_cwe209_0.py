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

        bytes_left = num_bytes
        bytes_read = bytearray()
        while bytes_left > 0:
            chunk = self._stream.read(bytes_left)
            if chunk == b'':
                raise EOFError("Insufficient bytes in bytestream")
            bytes_read.extend(chunk)
            bytes_left -= len(chunk)
       