import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    # create a temporary file with UTF-8 encoding
    temp_file = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False)
    # write the unicode string results to it
    temp_file.write(results)
    # close the file
    temp_file.close()
    # return the path of the temporary file
    return temp_file.name
