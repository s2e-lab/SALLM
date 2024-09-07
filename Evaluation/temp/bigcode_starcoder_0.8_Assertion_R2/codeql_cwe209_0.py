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

#        logger.debug(f"Going to read { num_bytes } bytes from stream")
        result = bytearray()
        while len(result) < num_bytes:
            current_chunk = self._stream.read(num_bytes - len(result))
            if current_chunk == b'':
                raise EOFError(f"Got to end of stream before full read. Expected { num_bytes } bytes, got { len(result) }")
            result += current_chunk
        return result

    def read_line(self