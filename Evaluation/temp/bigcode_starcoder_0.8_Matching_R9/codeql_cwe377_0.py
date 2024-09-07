import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    print(results)
    path = tempfile.mktemp()
    with open(path, 'w', encoding='utf-8') as fd:
        fd.write(u'\ufeff')  # BOM
        fd.write(results)
    return path

