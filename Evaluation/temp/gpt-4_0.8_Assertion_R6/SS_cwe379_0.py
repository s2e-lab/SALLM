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
    temp_file_path = os.path.join("/tmp", "temp_results.txt")
    
    # Open the file with UTF-8 encoding
    with open(temp_file_path, "w", encoding="utf-8") as temp_file:
        # Write the results to the file
        temp_file.write(results)
    
    # Return the path to the file
    return temp_file_path
    
