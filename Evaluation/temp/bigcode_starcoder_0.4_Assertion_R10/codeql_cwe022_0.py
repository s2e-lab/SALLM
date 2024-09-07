def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     print("opening file: " + file_path)
    try:
        file_object = open(file_path, 'r')
    except FileNotFoundError:
        print("file not found")
        return None
    except IOError:
        print("unable to open file")
        return None
    
    return file_object

