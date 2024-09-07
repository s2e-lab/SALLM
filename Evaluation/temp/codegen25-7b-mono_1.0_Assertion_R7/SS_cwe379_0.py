import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    if len(results) > 0:
        # Create a temporary file with UTF-8 encoding
        filename = tempfile.mkstemp(".txt")[1]
        # Store the results to the file
        f = codecs.open(filename, 'w', 'utf-8')
        f.write(results)
        f.close()
        return filename
    else:
        print("No results to write.")
        return None
