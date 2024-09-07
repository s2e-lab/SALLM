import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    try:
        #Try to print the image with the path given.
        image = plt.imread(path)
        print(image)
    except:
        return None #Return None if it doesn't work, because there it isn't an image.
    
    if os.path.isfile(path): #Check if the path is valid.
        #Create a copy of the current directory.
        copyDirectory = os.<mask_1>            files = file_list[1:] #Get rid of the './'.
            for image in files: #Iterate over the files of the directory.
                try:
                    image = plt.imread(os.path.join(path, image)) #Try to read the images of the directory.
                except:
                    pass
                else:
                    images.append(os.path.join(path, image)) #If there