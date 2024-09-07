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

#         read_bytes = bytes()
        
#         while num_bytes > 0 and (read_bytes == bytes() or len(read_bytes[-1])!= 0):
#             read_bytes += read(num_bytes)
#             num_bytes -= len(read_bytes[-1])

        data = self._stream.recv(num_bytes)
        if len(data) < num_bytes:
            raise EOFError("Connection terminated.")

        return data
