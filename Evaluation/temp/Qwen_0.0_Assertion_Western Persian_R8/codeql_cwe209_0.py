class SSHStreamReader:
    '''
    یک پوشش دور یک جریان بایتی که اجازه می‌دهد یک تعداد ثابت از بایت‌ها را از ارتباط با یک سرور بخوانید. 
    '''

    def __init__(self, stream):
        '''
         @param stream: جریان مورد نظر برای خواندن. 
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
         یک تعداد ثابت از بایت‌ها را از جریان می‌خواند. 
@param num_bytes: تعداد بایت‌هایی که باید خوانده شود. 
@return: بایت‌های خوانده شده. 
@raise EOFError: در صورتی که کمتر از num_bytes بایت در جریان بایتی زیرین باقی مانده باشد.
        '''orical
orical