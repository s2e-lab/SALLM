import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    _, tmp_file_path = tempfile.mkstemp(text=True)
    with codecs.open(tmp_file_path, 'w', encoding='utf-8') as tmp_file:
        tmp_file.write("\n")
        tmp_file.writelines(results)
        tmp_file.write("\n")
    return tmp_file_path

