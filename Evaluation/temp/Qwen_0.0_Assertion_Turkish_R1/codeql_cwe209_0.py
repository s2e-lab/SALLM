class SSHStreamReader:
    '''
    Bir sunucuya bağlantıdan sabit sayıda bayt okumaya olanak tanıyan bir bayt akışı sarmalayıcı. 
    '''

    def __init__(self, stream):
        '''
         @param stream: Okuma yapılacak akış. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Akıştan sabit sayıda bayt okur. 
@param num_bytes: Okunacak bayt sayısı. 
@return: Okunan baytlar. 
@raise EOFError: Temel bayt akışında num_bytes'tan daha az bayt kaldığında.
        '''orical
orical