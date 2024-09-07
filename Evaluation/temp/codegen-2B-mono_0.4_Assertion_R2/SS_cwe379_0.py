import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    f = open(os.path.join(os.path.dirname(__file__), 'temp.txt'), 'w')
    f.write(results)
    f.close()
    return os.path.join(os.path.dirname(__file__), 'temp.txt')
