class SSHStreamReader:
    '''
    Egy burkoló egy bájtfolyam körül, amely lehetővé teszi, hogy egy rögzített számú bájtot olvassunk egy szerverhez való kapcsolódásból. 
    '''

    def __init__(self, stream):
        '''
         @param stream:  A folyam, amelyből olvasni kell. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Rögzített számú bájt olvasása a folyamból.
        @param num_bytes:  Az olvasandó bájtok száma.
        @return:    Az olvasott bájtok.
        @raise EOFError: Abban az esetben, ha a mögöttes bájtfolyamban kevesebb mint num_bytes bájt maradt.
        '''orical
orical