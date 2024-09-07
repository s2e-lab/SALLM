import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    temp_file = os.path.join(os.getcwd(), "temp.py")
    f = open(temp_file, "w", encoding = "UTF-8")
    f.write(results)
    f.close()
    return temp_file

# In this case, we do not need to use the write_results function,
# because we don't need to do anything with the results except to print them.
