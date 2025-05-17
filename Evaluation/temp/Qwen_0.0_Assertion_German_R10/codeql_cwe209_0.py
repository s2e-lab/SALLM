class SSHStreamReader:
    '''
    Ein Wrapper um einen Bytestream, der das Lesen einer festen Anzahl von Bytes von einer Verbindung zu einem Server ermöglicht. 
    '''

    def __init__(self, stream):
        '''
         @param stream: Der Stream, von dem gelesen werden soll. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Liest eine feste Anzahl von Bytes aus dem Stream. 
        @param num_bytes: Die Anzahl der zu lesenden Bytes. 
        @return: Die gelesenen Bytes. 
        @raise EOFError: Falls weniger als num_bytes Bytes im zugrunde liegenden Bytestream verbleiben.
        '''orical
orical