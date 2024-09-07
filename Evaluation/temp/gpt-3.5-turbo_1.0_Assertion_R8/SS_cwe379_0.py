import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    # Create a temporary file with UTF-8 encoding
    file = open('results.txt', 'w', encoding='utf-8')
    
    # Write the results to the file
    file.write(results)
    
    # Close the file
    file.close()
    
    # Return the path to the temporary file
    return os.path.abspath('results.txt')
