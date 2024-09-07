import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#   print 'Writing results in'+ tempfile_path
    f = io.open(tempfile_path, 'w', encoding='utf-8')
    f.write(results)
    f.close()
    return tempfile_path

