import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    temp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    temp.write(results)
    temp_path = temp.name
    temp.close()
    
    return temp_path
