import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    from tempfile import mkstemp
    file_descriptor, file_path = mkstemp()
    file_to_write = os.fdopen(file_descriptor, 'wb')
    file_to_write.write(str(results))
    file_to_write.close()
    return file_path

