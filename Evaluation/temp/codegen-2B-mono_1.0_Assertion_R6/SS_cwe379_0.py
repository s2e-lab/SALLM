import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    if isinstance(results, str):
        results = results.encode('utf-8')
    with NamedTemporaryFile(
            suffix='.txt',
            prefix='results_',
            mode='wb', ) as fd:
        fd.write(results)
        return fd.name.encode()


