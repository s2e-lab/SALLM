import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

# todo: remove this
    with tempfile.NamedTemporaryFile('w+', encoding='utf-8', suffix='.py') as file_obj:
        file_obj.write(results)
        return file_obj.name

