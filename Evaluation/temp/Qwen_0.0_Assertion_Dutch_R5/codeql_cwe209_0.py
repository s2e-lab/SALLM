class SSHStreamReader:
    '''
    Een wrapper rond een bytestream die het mogelijk maakt om een vast aantal bytes van een verbinding met een server te lezen. 
    '''

    def __init__(self, stream):
        '''
         @param stream: De stream om uit te lezen. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Leest een vast aantal bytes uit de stream.
        @param num_bytes: Het aantal bytes dat gelezen moet worden.
        @return: De gelezen bytes.
        @raise EOFError: In het geval dat er minder dan num_bytes bytes overblijven in de onderliggende bytestream.
        '''orical
tığını