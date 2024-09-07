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

#        def read_to_end():
#            return b''.join(self._stream.iter_content(chunk_size=133*1024))

        return self._stream.read(num_bytes)
        result = self._stream.read(num_bytes)
        print(f'read bytes: {result}')

        if len(result)!= num_bytes:
            raise EOFError()
        else:
            return result

