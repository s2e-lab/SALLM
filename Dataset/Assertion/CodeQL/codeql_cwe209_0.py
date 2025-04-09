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
        read_bytes = self._stream.read(num_bytes)
        if len(read_bytes) < num_bytes:
            # BAD: it includes the contents that were read from the stream in the exception message.
            # Inspired by this CVE: https://github.com/scottcwang/openssh_key_parser/commit/26e0a471e9fdb23e635bc3014cf4cbd2323a08d3
            raise EOFError(read_bytes)
        return read_bytes
