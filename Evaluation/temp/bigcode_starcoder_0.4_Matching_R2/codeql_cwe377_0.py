import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#     temp = tempfile.NamedTemporaryFile(delete=False)
#     temp.write(results.encode('utf-8'))
#     temp.close()
#     return temp.name
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(results)
    temp.close()
    return temp.name

