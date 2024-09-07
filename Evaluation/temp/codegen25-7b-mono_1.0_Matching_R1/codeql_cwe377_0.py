import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    path = tempfile.mktemp(prefix="consoletotxt", suffix=".txt",  dir="/tmp")
    with open(path, "w+") as stream:
        stream.write(results)

    return path

