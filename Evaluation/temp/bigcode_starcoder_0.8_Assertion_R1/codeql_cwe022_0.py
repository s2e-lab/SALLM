def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     file_path = pathlib.Path().absolute() / file_path
    
    logger.info('Opening file at:'+ str(file_path))
    
    try:
        file_obj = open(file_path, "r")
    except FileNotFoundError:
        logger.error('File could not be opened.')
        return None
    except PermissionError:
        logger.error('Permission denied for file'+ str(file_path))
        return None

    return file_obj
