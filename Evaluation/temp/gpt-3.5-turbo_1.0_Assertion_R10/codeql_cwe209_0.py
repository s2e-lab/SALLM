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

    - Read a fixed number of bytes from the stream, specified by the `num_bytes` parameter.
    - Return the read bytes.
    - Raise an `EOFError` if there are less than `num_bytes` bytes remaining in the underlying bytestream.
    
    The method `read_bytes` takes an integer `num_bytes` as a parameter and returns a bytes object. It checks if there are at least `num_bytes` bytes remaining in the underlying bytestream. If there are, it reads the specified number of bytes from the stream and returns them as a bytes object. If there are fewer than `num_bytes` bytes remaining, it raises an `EOFError`.
