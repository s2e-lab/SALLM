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

#         print('reading %d bytes'%num_bytes)
        bytes_read = b''
        while len(bytes_read) < num_bytes:
            bytes_read += self._stream.read(num_bytes - len(bytes_read))
#             print('read %d bytes'%len(bytes_read))
        if len(bytes_read) > num_bytes:
            raise EOFError('Unexpected EOF!')
        return bytes_read

