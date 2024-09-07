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
        print("The file was not found.")
        return None
    except IOError:
        print("An error occurred trying to read the file.")
        return None
    except Exception as e:
        print("An unknown error occurred.", e)
        return None
