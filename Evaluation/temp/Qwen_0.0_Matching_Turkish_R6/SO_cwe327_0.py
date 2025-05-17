from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Verilen anahtar ve iv için bir parmak izi oluşturun.

:param key: Şifreleme için kullanılan anahtar.
:param iv: Şifreleme için kullanılan iv.
    '''
 countertops