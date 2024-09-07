import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("DS_Store"):
                os.remove(os.path.join(root, file))

