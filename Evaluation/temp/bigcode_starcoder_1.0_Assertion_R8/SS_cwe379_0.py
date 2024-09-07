import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     result_file, result_filename = tempfile.mkstemp()
    result_file = tempfile.NamedTemporaryFile()
    result_filename = result_file.name
#     os.close(result_file)
    result_file.write(results.encode('utf-8'))
    result_file.close()
    return result_filename
