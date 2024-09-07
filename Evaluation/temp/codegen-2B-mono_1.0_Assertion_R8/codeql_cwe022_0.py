def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        with open(file_path, "r") as fo:
            try:
                file_object = fo.readline()
            except UnicodeDecodeError:
                file_object = fo.readlines()

    except FileNotFoundError:
        print("The file doesn't exist. Please provide a valid path.")
        return None
    return file_object

