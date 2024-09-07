import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    f = tempfile.NamedTemporaryFile(
        prefix='tflite_convert_results_',
        dir=tempfile.gettempdir(),
        delete=False,
        mode='w+')
    f.write(results)
    f.close()
    return f.name

