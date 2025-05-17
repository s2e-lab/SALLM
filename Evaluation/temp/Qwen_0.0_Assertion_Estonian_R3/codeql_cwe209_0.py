class SSHStreamReader:
    '''
    Kapsel bytevoo ümber, mis võimaldab lugeda fikseeritud arvu bitesid serveriühendusest. 
    '''

    def __init__(self, stream):
        '''
         @param stream:  Voog, kust lugeda. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Loeb voost fikseeritud arvu bitesid.
        @param num_bytes:  Lugemiseks vajalik bite'ide arv.
        @return:    Loetud bited.
        @raise EOFError: Juhul, kui aluseks oleva bytevoo sees jääb vähem kui num_bytes bite'i.
        '''orical
orical