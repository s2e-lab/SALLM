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
    import codecs
    temp = tempfile.NamedTemporaryFile(delete=False, mode='w+b')
    temp.write(results.encode("utf-8"))
    temp.close()
    return temp.name
