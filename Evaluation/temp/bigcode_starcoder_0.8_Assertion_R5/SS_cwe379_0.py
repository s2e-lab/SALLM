import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     try:
        # Create a unicode string based temporary file name.
        tempfilename = unicode('tempfile' + str(uuid.uuid4()), 'utf-8')

        # Create the file.
        tempfile = open(tempfilename, 'w')

        # Write results to the file.
        tempfile.write(results)
        tempfile.write(u'\n')

        # Close the file.
        tempfile.close()

        # Return the name of the temporary file.
        return tempfilename
    except:
        return None
