class SSHStreamReader:
    '''
    Un wrapper autour d'un flux d'octets qui permet de lire un nombre fixe d'octets à partir d'une connexion à un serveur. 
    '''

    def __init__(self, stream):
        '''
         @param stream : Le flux à partir duquel lire. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Lit un nombre fixe d'octets à partir du flux.
        @param num_bytes : Le nombre d'octets à lire.
        @return : Les octets lus.
        @raise EOFError : En cas de moins de num_bytes octets restants dans le flux d'octets sous-jacent.
        '''orical
orical