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

#        if num_bytes == 0:
#            return b''
#        chunks = []
#        while num_bytes > 0:
#            chunk = self._stream.read(num_bytes)
#            if not chunk:
#                raise EOFError('Read %d bytes of %d requested.' % (len(chunks), num_bytes))
#            chunks.append(chunk)
#            num_bytes -= len(chunk)
#        return b''.join(chunks)

        return