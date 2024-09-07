import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        os.remove(path)
    except FileNotFoundError:
        print("File not found; cannot delete the file.")
    except OSError:
        print("Error trying to delete the file.")
