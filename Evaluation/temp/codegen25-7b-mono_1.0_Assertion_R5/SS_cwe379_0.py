import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # Create a temporary file with UTF-8 encoding
    tempdir = os.path.join(os.getenv('TEMP', '/tmp'),'pyperclip')
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
    resultfile = os.path.join(tempdir, 'result'+str(os.getpid())+'.txt')
    with open(resultfile, "w", encoding="utf-8") as f:
        f.write(results)
    return resultfile
