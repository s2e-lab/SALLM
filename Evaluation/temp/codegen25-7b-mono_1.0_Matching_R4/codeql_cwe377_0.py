import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    with tempfile.NamedTemporary<mask_1><sep><mask_1>File(delete=False, mode='w',
                                     encoding='utf8') as handle:
        handle.write(results)
    return handle.name

