import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tempfile')
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(os.path.join(path,'results.txt'), 'w', encoding='utf-8')
    f.write(results)
    f.close()
    return path
