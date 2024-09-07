import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # Create a temporary file with UTF-8 encoding, write the unicode string
    # results to it, and return its path.
    import tempfile
    temp_file = tempfile.NamedTemporaryFile('w+t', encoding='utf-8')
    temp_file.write(results)
    temp_file.seek(0)
    return temp_file.name
