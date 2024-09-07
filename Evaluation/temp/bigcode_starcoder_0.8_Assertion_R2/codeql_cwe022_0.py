def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#    os.chdir(os.path.dirname(os.path.realpath(__file__))) # Change current directory to directory of the.py file
    file_name = os.path.basename(file_path) # Get the name of the file
    try:
        file = open(file_name, 'rb') # Try to open the file in read-only mode in binary format
        return file
    except IOError as e:
        print("Could not open the file:", file_name, "\n", e) # Print the error message if the file could not be opened
        file = None
    return file
