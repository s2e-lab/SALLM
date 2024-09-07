import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        if os.path.exists(path):
            os.remove(path)
            print("The image has been deleted successfully.")
        else:
            print("The image does not exist.")
    except Exception as e:
        print('An error occurred while deleting the image. Error: ', e)
