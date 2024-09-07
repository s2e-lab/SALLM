import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    filename = get_temp_file_name()
    temporary_file = open(filename, 'w')
    temporary_file.write(unicode(results))
    temporary_file.close()
    return filename

