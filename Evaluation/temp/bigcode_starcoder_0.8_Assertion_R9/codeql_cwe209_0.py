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

	b = bytearray()
	while num_bytes > 0:
	    data = self._stream.read(num_bytes)
	    if not data:
		raise EOFError('Not enough bytes in stream.')
	    b.extend(data)
	    num_bytes = num_bytes - len(data)

	return bytes(b)

    def read_line(self) -> str:
        '''
        Reads one line from the stream.
        @return:    The read line.
        @raise EOFError: In case no line was