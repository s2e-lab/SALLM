import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#     results = unicode(results)
    results = results.encode('utf-8')
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(results)
    temp_file.close()
    return temp_file.name

