import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # Create a temporary file
    temp_file_path = os.path.join(os.getcwd(), 'temp.txt')
    
    # Open the file with write permissions and UTF-8 encoding
    with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        # Write the results to the file
        temp_file.write(results)
    
    # Return the path to the temporary file
    return temp_file_path
