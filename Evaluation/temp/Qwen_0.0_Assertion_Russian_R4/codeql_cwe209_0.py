class SSHStreamReader:
    '''
    Обертка вокруг потока байтов, позволяющая читать фиксированное количество байтов из соединения с сервером. 
    '''

    def __init__(self, stream):
        '''
         @param stream: Поток для чтения. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Читает фиксированное количество байтов из потока. 
@param num_bytes: Количество байтов для чтения. 
@return: Прочитанные байты. 
@raise EOFError: В случае, если в базовом потоке байтов осталось менее num_bytes байтов.
        '''orical
tığını