import re

def match_string(target_string):
    '''
    Girdi dizesinin aşağıdaki formatta geçerli bir dize olup olmadığını kontrol edin: x.y.z (x, y, z dizelerdir)

    :param hedef_dize: Kontrol edilecek dize
    :return: Dize geçerliyse True, aksi takdirde False

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını