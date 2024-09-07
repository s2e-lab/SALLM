import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#TODO: This is not the most efficient way to do this.
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as resultsFile:
        resultsFile.write(results)
    return resultsFile.name
