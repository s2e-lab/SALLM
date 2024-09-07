import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''


#    with open(os.path.join(
#        os.path.dirname(os.path.realpath(__file__)),
#       'results.txt'), 'w') as f:
#        f.write(results)

    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as f:
        f.write(results)
    return f.name

