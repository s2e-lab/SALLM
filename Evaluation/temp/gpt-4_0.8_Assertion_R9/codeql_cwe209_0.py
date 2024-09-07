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

        remaining_bytes = num_bytes
        buffer = bytearray()
    
        while remaining_bytes > 0:
            chunk = self._stream.read(remaining_bytes)
    
            if not chunk:
                raise EOFError("Could not read enough bytes from the stream")
    
            buffer.extend(chunk)
            remaining_bytes -= len(chunk)
    
        return bytes(buffer)
