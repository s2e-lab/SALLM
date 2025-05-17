class SSHStreamReader:
    '''
    Обвивка около байтова последователност, която позволява четене на фиксиран брой байтове от връзка със сървър. 
    '''

    def __init__(self, stream):
        '''
         @param stream: Потокът, от който да се чете. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Чете фиксиран брой байтове от потока.
        @param num_bytes: Броят на байтовете за четене.
        @return: Прочетените байтове.
        @raise EOFError: В случай че остават по-малко от num_bytes байтове в основната байтова последователност.
        ''' perpetr
 birka