import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

	for item in os.listdir(os.curdir):
        if item.endswith(path):
            os.remove(item)
