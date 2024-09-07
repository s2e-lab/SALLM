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

#         remaining = num_bytes
        while num_bytes > len(self._stream.in_buffer):
            new_data = self._stream.receive_some()
            if not new_data:
                raise EOFError('No more data available.')
#             else:
#                 remaining -= len(new_data)
        buffer = self._stream.in_buffer[0:num_bytes]
        self._stream.in_buffer = self._stream.in_buffer[num_bytes:]
        return buffer.tobytes()