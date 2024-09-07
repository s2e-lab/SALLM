import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    with codecs.open(os.path.join(os.path.dirname(__file__), '_results.txt'), 'w', encoding='utf-8') as results_file:
    with codecs.open('_results.txt', 'w', encoding='utf-8') as results_file:
        results_file.write(results)

    return '_results.txt'
