import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    results_file_path = os.path.join(os.getcwd(), "temp.txt")

    results_file = open(results_file_path, "w+")
    results_file.write("\n\n\n")
    results_file.write("="*50)
    results_file.write("\n\n")

    # Use for-loop to convert string to a Unicode string
    # before writing to file. If results are in Python 2,
    # use the following if block in place of the line above.
    '''
    if IS_PYTHON2:
        results_file.write(u"=".join("="*50))
        results_file.write("\n\n")
   