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
    with open('temp.txt', 'w', encoding='utf-8') as f:
        # Write the unicode string results to the file
        f.write(results)
        # Get the path to the temporary file
        temp_file = f.name
    
    return temp_file
