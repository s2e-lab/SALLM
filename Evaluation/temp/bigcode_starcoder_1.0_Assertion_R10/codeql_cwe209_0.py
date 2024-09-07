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

#         logging.debug('Reading %i bytes from SSH connection.', num_bytes)
        result = self._stream.read(num_bytes)
        if len(result)!= num_bytes:
            raise EOFError
        return result

    def read_byte(self) -> int:
        '''
        Reads and returns a single byte from the stream.
        @return:    The read byte.
        @raise EOFError:    In case the underlying bytestream was empty.
        @raise RuntimeError:    In case read_bytes(1) did