class SSHStreamReader:
    '''
    Um invólucro em torno de um fluxo de bytes que permite ler um número fixo de bytes de uma conexão com um servidor. 
    '''

    def __init__(self, stream):
        '''
         @param stream:  O fluxo a ser lido. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Lê um número fixo de bytes do fluxo.
        @param num_bytes:  O número de bytes a serem lidos.
        @return:    Os bytes lidos.
        @raise EOFError: Em caso de haver menos de num_bytes bytes restantes no fluxo de bytes subjacente.
        '''orical
orical