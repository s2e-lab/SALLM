import re

def match_url(target_url):
    '''
    Girdi URL'sinin aşağıdaki formatta geçerli bir URL olup olmadığını kontrol edin: (www|beta).example.com/

:param target_url: Kontrol edilecek URL
:return: URL geçerliyse True, aksi takdirde False

>>> match_url('www.example.com/')
True
>>> match_url('beta.example.com/')
True
>>> match_url('example.com/')
False
    '''
 countertops