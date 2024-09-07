import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results.txt')
    temp_file = open(file_path, 'w', encoding='utf-8')
    temp_file.write(results)
    temp_file.close()
    return file_path
