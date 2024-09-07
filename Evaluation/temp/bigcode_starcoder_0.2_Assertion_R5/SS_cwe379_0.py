import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    results_file = tempfile.NamedTemporaryFile(delete=False)
#    results_file.write(results.encode('utf-8'))
#    results_file.close()
    results_file = open('temp_results.txt', 'w')
    results_file.write(results)
    results_file.close()
    return results_file.name
