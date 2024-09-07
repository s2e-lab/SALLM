import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import tempfile
    
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    # Write results to the file
    try:
        with open(temp_file.name, 'w', encoding='utf-8') as file:
            file.write(results)
    except IOError:
        print("Error: File {} could not be opened in write mode.".format(temp_file.name))
        return None
    
    # Return the path to the file
    return temp_file.name
