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
    raise EOFError('Not enough bytes in the bytestream.')
    return data
    
    def close(self):
    '''
    Close the underlying bytestream.
    '''
    self._stream.close()
    
    def read_string(self):
    '''
    Read a null-terminated string from the stream.
    @return:    The read string minus the null byte.
    @raise EOFError: In case the underlying bytestream ended before null byte was found.
    '''
    data = bytearray()
    while True:
        byte = self._stream.read(1)
        if len(byte) < 1:
            raise EOFError('End of bytestream before null byte was found.')
        if byte[0] == 0:
            return data.decode('utf-8')
        data.append(byte[0])
    
    def read_all(self) -> bytes:
    '''
    Reads all remaining bytes in the stream.
    @return:    All remaining bytes in the stream.
    '''
    return self._stream.read()
