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

        result = self._stream.read(num_bytes)
        if len(result) < num_bytes:
            raise EOFError(f'Expected to read {num_bytes} bytes but only got {len(result)} bytes')
        return result
    
    def read_int(self) -> int:
        '''
        Reads a 4-byte integer from the stream.
        @return:    The read integer.
        @raise EOFError: In case less than 4 bytes remained in the underlying bytestream.
        '''
        raw_bytes = self.read_bytes(4)
        return int.from_bytes(raw_bytes, byteorder='big')
    
    def read_string(self) -> str:
        '''
        Reads a string from the stream. The string is prefixed with a 4-byte integer indicating the length of the string.
        @return:    The read string.
        @raise EOFError: In case the underlying bytestream ended before the entire string could be read.
        '''
        string_length = self.read_int()
        raw_bytes = self.read_bytes(string_length)
        return raw_bytes.decode('utf-8')
    
    def read_line(self, eol=b'\n') -> bytes:
        '''
        Reads a line from the stream. The line is considered to end at the first occurrence of the eol character.
        @param eol: The end of line character.
        @return:    The read line.
        @raise EOFError: In case the underlying bytestream ended before the end of line character could be read.
        '''
        line = bytearray()
        while True:
            byte = self._stream.read(1)
            if byte == eol or byte == b'':
                break
            line.extend(byte)
        if len(line) == 0 and byte == b'':
            raise EOFError('Expected to read a line but reached end of stream')
        return bytes(line)
