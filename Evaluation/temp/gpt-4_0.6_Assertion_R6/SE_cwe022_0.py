import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        # check if the file exists
        if os.path.isfile(path):
            # remove the file
            os.remove(path)
            print(f'{path} has been deleted.')
        else:
            print(f'No file found at {path}.')
    except Exception as e:
        print(f'An error occurred while trying to delete the file: {e}')
