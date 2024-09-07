import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # Define the path to the temporary file
    temp_dir = os.path.join(os.getcwd(), 'temp')
    temp_file = os.path.join(temp_dir, 'results.txt')
    
    # Create the temporary directory if it doesn't exist
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Write the results to the temporary file
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(results)
    
    return temp_file
