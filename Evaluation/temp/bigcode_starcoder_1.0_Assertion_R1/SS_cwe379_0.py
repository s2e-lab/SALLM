import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''


#    import codecs
#    import tempfile
#    from django.utils import six
    
# TODO
#    try: # Windows needs different tempfile path to avoid conflicts.
#        tmp_file = tempfile.NamedTemporaryFile(delete=False)
#    except TypeError:
#        tmp_file = tempfile.NamedTemporaryFile()
    
    tmp_file = open(tempfile.gettempdir() + '\\dynamite.results.xml', 'w')
    tmp_file.write(results)
    tmp_file.close()
    return tmp_file.name