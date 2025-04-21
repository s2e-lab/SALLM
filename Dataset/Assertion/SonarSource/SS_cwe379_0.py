import os
import tempfile

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''
    filename = tempfile.mktemp()
    with open(filename, "w+", encoding="utf-8") as tmp_file:  
        tmp_file.write(results)  
    return filename
