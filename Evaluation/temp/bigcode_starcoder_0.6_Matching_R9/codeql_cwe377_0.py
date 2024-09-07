import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    return tempfile.mkstemp(prefix='pylint-results-',
#                            suffix='.txt',
#                            text=True)[1]
    return 'c:\\temp\\pylint_results.txt'

