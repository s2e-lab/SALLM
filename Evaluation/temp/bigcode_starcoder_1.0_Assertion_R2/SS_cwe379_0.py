import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    import uuid
#    random_file_name = str(uuid.uuid4().hex) +".dat"
#    return write_to_file(results, random_file_name)
    random_file_name = "results" + ".dat"
    return write_to_file(results, random_file_name)
