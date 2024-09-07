import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     import tempfile
#     tmp_file = tempfile.NamedTemporaryFile(delete=False)
#     tmp_file.write(results.encode('utf-8'))
#     tmp_file.close()
#     return tmp_file.name
    import uuid
    tmp_file = os.path.join(os.path.dirname(__file__), 'tmp', str(uuid.uuid4()))
    with open(tmp_file, 'w') as f:
        f.write(results)
    return tmp_file
