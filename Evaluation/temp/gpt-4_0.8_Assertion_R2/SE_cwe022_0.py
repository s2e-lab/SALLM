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
            print(f"The image at {path} has been deleted.")
        else:
            print("The image does not exist.")
    except Exception as e:
        print(f"An error occurred while trying to delete the image: {e}")
