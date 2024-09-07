import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        # check if file exists
        if os.path.exists(path):
            os.remove(path)
            print(f"{path} has been deleted.")
        else:
            print(f"No such file: {path}")
    except Exception as e:
        print(f"An error occurred while deleting {path}. Error: {str(e)}")
