import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    _, file_path = tempfile.mkstemp(suffix=".txt", encoding="utf-8")
    with open(file_path, "w") as file:
        file.write(results)
    return file_path

