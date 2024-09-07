import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import codecs
    import tempfile
    file_name = next(tempfile._get_candidate_names())
    temp_file = os.path.join(tempfile.gettempdir(), '{}.tmp'.format(file_name))
    with codecs.open(temp_file, 'w', 'utf-8') as f:
        f.write(results)
    return temp_file
