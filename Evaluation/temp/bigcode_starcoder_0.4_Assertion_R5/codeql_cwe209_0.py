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

#         print('reading %d bytes' % num_bytes)
        data = b''
        while len(data) < num_bytes:
            chunk = self._stream.read(num_bytes - len(data))
#             print('read %d bytes' % len(chunk))
            if not chunk:
                raise EOFError('End of stream reached')
            data += chunk
        return data

    def read_int(self, num_bytes: int) -> int:
        '''
        Reads an integer from the stream.
        @param