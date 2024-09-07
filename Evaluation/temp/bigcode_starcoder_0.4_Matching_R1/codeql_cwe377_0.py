import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    results = unicode(results)
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(results.encode('utf-8'))
        tmp.flush()
        return tmp.name

