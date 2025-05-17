import re

def match_string(target_string):
    '''
    Narito ang pagsasalin ng iyong ibinigay na teksto sa Tagalog:

Suriin kung ang input na string ay isang wastong string na may sumusunod na format: x.y.z (x, y, z ay mga string)

    :param target_string: Ang string na susuriin
    :return: True kung ang string ay wasto, False kung hindi

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
tığını