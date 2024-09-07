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

        # Check to make sure that we don't try to read bytes past the buffered data.
        data = self._stream.read(num_bytes)
        self._stream.unread(data)
        # If we have not read the required data yet, it means that we didn't read the complete message.
        if len(data) < num_bytes:
            raise EOFError()
        