import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import tempfile

    # create a temporary file
    tmp_file = tempfile.NamedTemporaryFile()
    tmp_path = tmp_file.name
    # open the file for write
    f = open(tmp_path, "w+", encoding='utf-8')
    # write results to file and close it
    f.write(results)
    f.close()

    return tmp_path

