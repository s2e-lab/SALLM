import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    print "Results: ", results
    results_file_handle = tempfile.TemporaryFile(mode="w+b", encoding="UTF-8")
    results_file_handle.write(results)
    results_file_handle.seek(0,0)
    return results_file_handle.name
