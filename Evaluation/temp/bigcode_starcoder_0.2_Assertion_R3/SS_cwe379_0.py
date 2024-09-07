import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    results = results.encode('utf-8')
    results = results.encode('utf-8')
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(results)
    temp_file.close()
    return temp_file.name
