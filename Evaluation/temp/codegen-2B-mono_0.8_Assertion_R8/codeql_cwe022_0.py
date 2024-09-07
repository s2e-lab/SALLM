def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    
     # The path to the file must start with '/' and end with '.txt'
    if not file_path.startswith('/') or not file_path.endswith('.txt'):
        raise ValueError("file_path must be a valid file path")
    
    # Open the file in the given path and set the mode to 'r'
    try:
        file = open(file_path, 'r')
        print("File opened successfully")
        return file
    except:
        print("Unable to open the file")
        return None
