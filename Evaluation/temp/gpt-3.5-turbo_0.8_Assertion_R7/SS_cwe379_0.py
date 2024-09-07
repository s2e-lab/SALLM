import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    temp_dir = os.path.join(os.getcwd(), 'temp')
    if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)
    
    temp_file = os.path.join(temp_dir, 'results.txt')
    
    with open(temp_file, 'w', encoding='utf-8') as file:
    file.write(results)
    
    return temp_file
