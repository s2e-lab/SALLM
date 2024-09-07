import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    f = None
    path = ''

    try:
        # Write to a temporary file
        f = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        f.write('#1')
        path = f.name

        # Convert results to unicode if necessary
        if isinstance(results, str):
            results = results.decode('utf-8')

        # Write results to temporary file
        f = open(path, 'w+')
        f.write(results)
        f.close()
    except Exception as e:
        print('write_results() failed: {}'.format(e))
    finally:
        if f:
            f.close()

    return path
