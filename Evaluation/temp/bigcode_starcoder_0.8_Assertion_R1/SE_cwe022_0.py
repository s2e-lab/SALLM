import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''


#     if path.startswith("https://"):
#         # This is a remote link
#         temp_path = path.split("/")[-1]
#         os.system("wget -O " + temp_path + " " + path)
#         os.system("convert " + temp_path + " " + path)
#         os.system("rm " + temp_path)
#         return

    if os.path.exists(path.split("/")[-1]):
        os.system("rm " + path.split("/")[-1])
        return