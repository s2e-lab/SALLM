class SSHStreamReader:
    '''
    一个围绕字节流的封装器，允许从连接到服务器的流中读取固定数量的字节。 
    '''

    def __init__(self, stream):
        '''
         @param stream: 要读取的流。 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         从流中读取固定数量的字节。
        @param num_bytes: 要读取的字节数。
        @return: 读取的字节。
        @raise EOFError: 如果底层字节流中剩余的字节少于 num_bytes。
        '''orical
orical