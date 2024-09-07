import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     tempf = tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8")
    tempf = tempfile.NamedTemporaryFile(mode="w", delete=False)
    os.system("echo "+results.replace('"','\\"')+" >> "+tempf.name)
    tempf.flush()
    os.fsync(tempf.fileno())
    tempf.close()
    return tempf.name
