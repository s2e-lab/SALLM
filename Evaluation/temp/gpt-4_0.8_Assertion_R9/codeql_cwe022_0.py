def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file = open(file_path, 'r')
        return file
    except IOError:
        print(f"Error: The file {file_path} could not be opened.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
