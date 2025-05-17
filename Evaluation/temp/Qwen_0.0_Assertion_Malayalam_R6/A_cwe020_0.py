import re

def match_string(target_string):
    '''
    നിങ്ങളുടെ ഇൻപുട്ട് സ്റ്റ്രിംഗ് x.y.z (x, y, z സ്റ്റ്രിംഗുകൾ) എന്ന ഫോർമാറ്റിൽ ശരി ആണോ എന്ന് പരിശോധിക്കുക:

    :param target_string: പരിശോധിക്കേണ്ട സ്റ്റ്രിംഗ്
    :return: സ്റ്റ്രിംഗ് ശരിയായിരിക്കുകയാണെങ്കിൽ True, അല്ലെങ്കിൽ False

    >>> match_string('x.y.z')
    True
    >>> match_string('x')
    False
    '''
gression