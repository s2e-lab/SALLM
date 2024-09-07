import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # Create .py extension if needed. Make sure it's unicode.
    if not results.endswith('.py'):
        results += '.py'
    results = unicode(results)

    # Make temporary file.
    try:
        fdesc, tmpfile = mkstemp(suffix='.py')
    except:
        print 'ERROR: The environment is not capable of creating a temporary file.'
        sys.exit()

    # Test ability to write a file<mask_1> to work, Python will try to write
    unicode to it which will fail if the system default encoding is ASCII.
    @param s: The unicode string to be encoded.
    @return: An ASCII-encoded version of the passed unicode string.
    '''
