import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    _, res_file_path = tempfile.mkstemp(".txt")

    with io.open(res_file_path, 'w', encoding='utf-8') as f:
        f.write(results)

    return res_file_path

