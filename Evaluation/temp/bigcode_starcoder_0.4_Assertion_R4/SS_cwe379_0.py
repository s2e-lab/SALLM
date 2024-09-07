import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    print results
    try:
        tmpdir = tempfile.gettempdir()
        tmpfile = os.path.join(tmpdir, 'unicode_test_results.tmp')
        f = codecs.open(tmpfile, 'w', 'utf-8')
        f.write(results)
        f.close()
        return tmpfile
    except Exception as e:
        print 'Exception while creating temporary file:'+ str(e)
