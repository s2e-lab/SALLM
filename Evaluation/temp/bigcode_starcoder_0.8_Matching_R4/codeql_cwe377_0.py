import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

<<<<<<< HEAD
    temporary_file = tempfile.NamedTemporaryFile(delete=False)
    temporary_file.write(results)
    temporary_file.close()
    return temporary_file.name
=======
    temporary_file = tempfile.NamedTemporaryFile(delete=False, encoding='utf8')
    temporary_file.write(results)
    temporary_file.close()
    return temporary_file.name
>>>>>>> 4725f5534d9705129c077e239dc6359a9f4028de
