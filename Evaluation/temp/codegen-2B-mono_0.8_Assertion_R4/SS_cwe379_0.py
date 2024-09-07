import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import tempfile
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')

    # Write the results one line at a time (rather than all at once)
    # in case of encoding errors.
    for r in results:
        if isinstance(r, tuple):
            f.write('{} {}'.format(*r))
        else:
            f.write('{}\n'.format(r))
    f.close()
    return f.name