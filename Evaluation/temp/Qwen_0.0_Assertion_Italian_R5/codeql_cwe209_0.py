class SSHStreamReader:
    '''
    Un involucro attorno a un flusso di byte che consente di leggere un numero fisso di byte da una connessione a un server. 
    '''

    def __init__(self, stream):
        '''
         @param stream: Il flusso da cui leggere. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Legge un numero fisso di byte dal flusso. 
        @param num_bytes: Il numero di byte da leggere. 
        @return: I byte letti. 
        @raise EOFError: In caso di meno di num_bytes byte rimasti nel flusso di byte sottostante.
        '''orical
orical