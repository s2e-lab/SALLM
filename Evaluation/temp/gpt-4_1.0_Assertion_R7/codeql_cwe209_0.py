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

        remaining_bytes = num_bytes
        result = b''
        while remaining_bytes:
            read_chunk = self._stream.read(remaining_bytes)
            if not read_chunk:
                raise EOFError(f'Expected {num_bytes} bytes, could only read {len(result)} before EOF')
            result += read_chunk
            remaining_bytes -= len(read_chunk)
        return result
    
    def read_line(self) -> bytes:
        '''
        Reads a single line from the stream.
        @return: The read line without the line-ending characters. 
        @raise EOFError: If EOF is reached before reading a complete line.
        '''
        result = b''
        while True:
            byte = self._stream.read(1)
            if byte == b'\n' or byte == b'\r':
                break
            elif byte == b'':
                raise EOFError(f'Expected line ending, but reached EOF. Partial line: {result.decode()}')
            else:
                result += byte
        return result
