def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    file_obj = None

    try:
        file_obj = open(file_path)
    except:
        print("An error occurred opening the file: ", file_path, " in the current directory.", file = sys.stderr)
        return None
    return file_obj
