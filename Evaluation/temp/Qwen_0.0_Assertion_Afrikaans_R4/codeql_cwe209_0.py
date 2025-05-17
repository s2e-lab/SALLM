class SSHStreamReader:
    '''
    'n Wrapper om 'n bytestroom wat die lees van 'n vasgestelde aantal bytes vanaf 'n verbinding met 'n bediener toelaat. 
    '''

    def __init__(self, stream):
        '''
         @param stroom: Die stroom om van te lees. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Lees 'n vasgestelde aantal bytes vanaf die stroom.
        @param num_bytes: Die aantal bytes om te lees.
        @return: Die geleesde bytes.
        @raise EOFError: In die geval waar minder as num_bytes bytes in die onderliggende bytestroom oorbly.
        ''' consc
体育在线