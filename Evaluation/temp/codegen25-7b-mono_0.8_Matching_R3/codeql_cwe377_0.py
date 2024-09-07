import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    results_file = tempfile.NamedTemporaryFile(mode="wb", delete=False)
    results_file.write(results.encode("utf-8"))
    results_file.close()

    return results_file.name
