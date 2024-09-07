import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    del_file_list = os.listdir(path)
    if not del_file_list:
        return
    for name in del_file_list:
        if name.endswith("jpg") or name.endswith("png") or name.endswith("gif"):
            os.remove(path + name)
