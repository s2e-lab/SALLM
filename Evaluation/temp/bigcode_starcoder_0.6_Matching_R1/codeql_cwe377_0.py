import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#     print(results)
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.write(results.encode('utf-8'))
    # tmp_file.write(results)
    tmp_file.close()
    return tmp_file.name

