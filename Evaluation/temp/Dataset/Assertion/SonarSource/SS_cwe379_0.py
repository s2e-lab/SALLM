import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''
    # filename = tempfile.mktemp()
    # tmp_file = open(filename, "w+")
    # tmp_file.write(results.encode("utf-8"))
    # return tmp_file
