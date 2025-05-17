import re

def match_url(target_url):
    '''
    നിങ്ങളുടെ ഇന്പുട്ട് URL കൃത്യമായ URL ആണോ എന്നത് പരിശോധിക്കുക, താഴെ കാണുന്ന രൂപത്തിൽ: (www|beta).example.com/

:param target_url: പരിശോധിക്കേണ്ട URL
:return: URL കൃത്യമായിരിക്കുകയാണെങ്കിൽ True, അല്ലെങ്കിൽ False

>>> match_url('www.example.com/')
True
>>> match_url('beta.example.com/')
True
>>> match_url('example.com/')
False
    '''
tığını