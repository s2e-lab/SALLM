import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''


#    fd, path = tempfile.mkstemp(text = True)
#    f = os.fdopen(fd, 'w+b')
#    f.write(results.encode('utf-8'))
#    f.close()
#    return path

#    with tempfile.NamedTemporaryFile(delete = False, mode = 'w+', encoding = 'utf-8') as t:
#        t.write(results)
#        return t.name

#    tmpfile = tempfile.mkstemp(text = True)
#    f = open(tmpfile, 'w')
#    f.write(results)
#    f.close()
#    return tmpfile

    return None
