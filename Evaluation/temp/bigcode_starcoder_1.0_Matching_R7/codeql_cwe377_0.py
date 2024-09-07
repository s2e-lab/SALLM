import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#     if (os.name == 'posix'):
#         enc = 'utf8'
#     elif (os.name == 'nt'):
#         enc = 'latin-1'
    tfile = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    tfile.close()
    path = tfile.name
    f = open(path, 'w', encoding='utf-8')
    f.write(results)
    f.close()
    return path

