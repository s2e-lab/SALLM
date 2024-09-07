import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    local_path = os.path.realpath(os.path.dirname(__file__))
    local_file = u'{}/../doc_output/test_results.txt'.format(local_path)
    with open(local_file,'w',encoding='utf-8') as fp:
        fp.write(results)
        fp.flush()
        fp.close()
    return local_file