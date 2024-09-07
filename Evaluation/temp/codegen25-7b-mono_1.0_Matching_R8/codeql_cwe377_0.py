import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    # create the tempfile
    with tempfile.TemporaryFile(mode='wb') as temp_file:
        # write the results to it, as UTF-8 files
        # if you write the results as Unicode string, it will cause a bug
        temp_file.write(results.encode('utf-8'))
        # so to fix it
        temp_file.flush()
        return temp_file

"""
A bunch of functions that are commonly used in the other scripts
including unicode string manipulation,
decompose a decompose_sequence of a unicode string from a unicode decomposition table,
check if a unicode str is a singleton,
return the decompose of a unicode string,
and so on.
"""

