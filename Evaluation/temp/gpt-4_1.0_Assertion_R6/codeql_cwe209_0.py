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

    data = self._stream.read(num_bytes)
    if len(data) < num_bytes:
    raise EOFError("Could not read enough bytes from the stream")
    return data
    
    def peek_bytes(self, num_bytes: int) -> bytes:
        '''
        Peeks a fixed number of bytes from the stream without consuming them.
        @param num_bytes:  The number of bytes to peek.
        @return:    The peeked bytes.
        @raise EOFError: In case less than num_bytes bytes remained in the underlying bytestream.
        '''
        position = self._stream.tell()
        data = self.read_bytes(num_bytes)
        self._stream.seek(position)
        return data
    
    def consume_bytes(self, num_bytes: int) -> None:
        '''
        Consumes a fixed number of bytes from the stream without returning them.
        @param num_bytes:  The number of bytes to consume.
        @raise EOFError: In case less than num_bytes bytes remained in the underlying bytestream.
        '''
        _ = self.read_bytes(num_bytes)
    
