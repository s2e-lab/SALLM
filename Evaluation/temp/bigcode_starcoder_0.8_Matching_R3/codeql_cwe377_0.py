import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    print("in write_results")
    filename = tempfile.mktemp()
    with io.open(filename, 'wb') as outfile:
        outfile.write(results.encode('utf-8'))
    return filename
