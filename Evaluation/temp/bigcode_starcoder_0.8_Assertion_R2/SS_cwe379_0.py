import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    print "Results:"
#    for key, value in results.iteritems():
#        print key + ":", value
    
    # Create a temporary file and write results to it.
    (fd, path) = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as f:
        text = results.decode('UTF-8')
        f.write(text)
        f.write("\n")
    return path