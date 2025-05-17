class SSHStreamReader:
    '''
    Một lớp bao quanh một luồng byte cho phép đọc một số byte cố định từ kết nối đến máy chủ. 
    '''

    def __init__(self, stream):
        '''
         @param stream:  Luồng để đọc từ đó. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         Đọc một số byte cố định từ luồng.
        @param num_bytes:  Số byte cần đọc.
        @return:    Các byte đã đọc.
        @raise EOFError: Trong trường hợp số byte còn lại trong luồng byte cơ bản ít hơn num_bytes.
        '''orical
orical