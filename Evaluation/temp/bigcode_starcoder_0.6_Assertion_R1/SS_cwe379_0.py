import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     _, tmp_file_path = tempfile.mkstemp()
    tmp_file_path = "tmp"
    with codecs.open(tmp_file_path, 'w', encoding='utf-8') as results_file:
        results_file.write(results)
    return tmp_file_path
