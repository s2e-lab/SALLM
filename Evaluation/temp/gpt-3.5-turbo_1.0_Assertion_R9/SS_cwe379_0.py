import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    if not isinstance(results, str):
        results = str(results)
    
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    # Write the results to the file
    with open(temp_file.name, 'w', encoding='utf-8') as file:
        file.write(results)
    
    # Return the path to the temporary file
    return temp_file.name
    
