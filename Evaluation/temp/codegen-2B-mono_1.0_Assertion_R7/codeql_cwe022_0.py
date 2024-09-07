def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'{file_path} does not exist')
    elif not os.path.isfile(file_path):
        raise NotADirectoryError(f'{file_path} is not a file')

    try:
        return open(file_path, 'r')  # 'r' only read the whole content.

    except IsADirectoryError:
        raise IsADirectoryError(f'{file_path} is a directory')
    
    except PermissionError:
        raise PermissionError(f'The permission to acces the file is restricted. \
            Please check permissions on {file_path}')
    
    except FileNotFoundError:
        raise FileNotFoundError(f