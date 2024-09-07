def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = open(file_path, 'r')
        return file
    except FileNotFoundError:
        print("The file does not exist in the given path.")
        return None
    except IOError:
        print("The file could not be opened.")
        return None
    except Exception as e:
        print("An unexpected error occurred while opening the file: ", e)
        return None
