import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    fd, path = tempfile.mkstemp('.txt', '', os.path.dirname(__file__))
    with io.open(fd, 'w', encoding='utf-8') as f:
        f.write(results)
    return path
