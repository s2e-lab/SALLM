import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    if os.path.exists(path): #If file exists, it deletes it:
        os.remove(path)

"""
The following script is used to generate the final CSV files and then used to extract the data from the final CSV files.
This script contains functionality to:
    1. Read raw data files for the following topics:
        - 1_final_output_v1.csv
        - 2_final_output_v2.csv
        - 3_final_output_v3.csv
        - 4_final_output_v4.csv
        - 6_final_output_v6.csv
        - 7_final_output_v7.csv
    2. Format the final data to a required format and formart it appropriately.
    3. Extract the required columns from the formatted CSV files (as specified in the format).
    4. Gener