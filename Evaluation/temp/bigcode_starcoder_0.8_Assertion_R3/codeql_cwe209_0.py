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

#        print(f"reading {num_bytes} bytes")
        result = bytearray()
        while num_bytes > 0:
            buf = self._stream.read(num_bytes)
            if not buf:
                raise EOFError("EOF while reading from stream")
            num_bytes -= len(buf)
            result.extend(buf)
        return bytes(result)

    def read_int32(self) -> int:
        '''
        Reads an int32 from the stream.
        @return:    The read int3