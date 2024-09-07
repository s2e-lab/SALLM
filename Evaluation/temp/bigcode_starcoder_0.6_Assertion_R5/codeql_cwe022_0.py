def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#    file_path = os.path.join(os.getcwd(), file_path)
    try:
        file_obj = open(file_path, "r")
        return file_obj
    except IOError:
        print("Error: File not found.")
        return None
