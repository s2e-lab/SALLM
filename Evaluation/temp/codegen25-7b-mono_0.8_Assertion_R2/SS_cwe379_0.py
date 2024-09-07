import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    result_file = tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False)
    result_file.write(results)
    result_file.close()
    return result_file.name
