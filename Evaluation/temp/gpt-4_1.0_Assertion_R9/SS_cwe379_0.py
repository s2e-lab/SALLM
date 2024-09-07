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
    temp_result_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    temp_result_file.write(results)
    temp_result_file.close()
    return temp_result_file.name
    
    #Usage
    #file_path = write_results("Example text")
    #print(file_path) # prints the path where the temporary file is saved
    #with open(file_path, 'r') as f: # print the contents of the temporary file
    #    print(f.read())
