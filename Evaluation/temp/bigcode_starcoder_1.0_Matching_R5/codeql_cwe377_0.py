import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

# This doesn't work. Only writes with 'utf-8' encoding, but it's UTF-16.
#    # Write the results to a temp file
#    with tempfile.NamedTemporaryFile() as tmpfile:
#        tmpfile.write(results.encode('utf-16'))
#        tmpfile.seek(0)
#        return tmpfile.name

    # Write the results to a temp file
    with tempfile.NamedTemporaryFile(suffix='.tsv') as tmpfile:
        tmpfile.write(results.encode('utf-8'))
        tmpfile.seek(0)
        return tmpfile.name


"""
============================================================================
============================================================================
============================================================================
"""

