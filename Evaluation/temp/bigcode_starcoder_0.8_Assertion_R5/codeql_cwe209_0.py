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

#        print("read_bytes({}, {})".format(num_bytes, self._stream.tell()))
        if num_bytes < 0:
            raise ValueError("The number of bytes to read must not be negative")
        if num_bytes == 0:
            return b''
        bytes_read = bytes()
        while len(bytes_read) < num_bytes:
            bytes_read += self._stream.read(num_bytes - len(bytes_read))
            if len(bytes_read) < num_bytes:
               