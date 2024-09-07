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

        # read the whole stream into memory
        data_read = self._stream.read(num_bytes)

        # check if we got all that
        if len(data_read) == num_bytes:
            # and remove from the stream
            self._stream.truncate(0)

        elif len(data_read) < (num_bytes - 1):
            # remove from