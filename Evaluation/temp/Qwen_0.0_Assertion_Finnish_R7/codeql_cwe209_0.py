class SSHStreamReader:
    '''
    Kääre bytestreamin ympärille, joka mahdollistaa kiinteän määrän tavujen lukemisen palvelinyhteydestä. 
    '''

    def __init__(self, stream):
        '''
         @param stream:  Lukemiseen käytettävä stream. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Lukee kiinteän määrän tavuja streamista.
        @param num_bytes:  Luettavien tavujen määrä.
        @return:    Luetut tavut.
        @raise EOFError: Jos pohjaisessa bytestreamissa on jäljellä vähemmän kuin num_bytes tavua.
        ''' perpetr
 perpetr