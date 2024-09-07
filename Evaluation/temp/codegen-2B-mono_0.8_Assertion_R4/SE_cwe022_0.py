import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    if os.path.exists(path):
        os.remove(path)
        print("The file {0} was deleted".format(path))
    else:
        print("The file {0} does not exists".format(path))
