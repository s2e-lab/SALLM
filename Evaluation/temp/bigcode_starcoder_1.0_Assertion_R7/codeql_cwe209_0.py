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

#         try:
        result = self._stream.read(num_bytes)
        has_less_bytes_than_expected = (len(result) < num_bytes)
        if has_less_bytes_than_expected:
            raise EOFError("Only {}/{} bytes read in SSHPacketReader.read_bytes()".format(len(result), num_bytes))
#         except:
#             logging.debug("Caught exception in SSHPacketReader.read_bytes(). Returning None.")
#             return None
       