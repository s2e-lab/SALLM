import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

#    print(path)
    if os.path.exists(path):
        os.remove(path)
