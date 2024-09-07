import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    results_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp/results.txt')
    results_path = os.path.join(os.path.realpath(os.path.dirname(__file__)),'results.txt')
    encoded_results = results.encode('utf-8')
    with codecs.open(results_path, 'w', 'utf-8') as results_file:
        results_file.write(encoded_results)
    return results_path
