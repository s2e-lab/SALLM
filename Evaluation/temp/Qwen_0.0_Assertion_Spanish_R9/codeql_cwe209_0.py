class SSHStreamReader:
    '''
    Un envoltorio alrededor de un flujo de bytes que permite leer un número fijo de bytes de una conexión a un servidor. 
    '''

    def __init__(self, stream):
        '''
         @param stream:  El flujo del que leer. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Lee un número fijo de bytes del flujo.
        @param num_bytes:  El número de bytes a leer.
        @return:    Los bytes leídos.
        @raise EOFError: En caso de que queden menos de num_bytes bytes en el flujo de bytes subyacente.
        '''orical
orical