import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

# 1. create a tmp file on disk
    with tempfile.NamedTemporaryFile(mode='w+t') as tf:
# 2. set encoding
        tf.write(results)
# 3. go to the beginning of the file
        tf.seek(0)
# 4. return the path of the file
        return tf.name
