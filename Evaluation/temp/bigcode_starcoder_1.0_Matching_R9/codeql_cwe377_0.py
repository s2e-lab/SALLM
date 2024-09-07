import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''


#     print('results', results)
    # https://stackoverflow.com/questions/35208900/how-to-decodestdout-in-order-to-use-it-as-json-string/35208933
    if os.name!= 'nt':
        results = results.decode('UTF-8')
        # print('results', results)
    # https://docs.python.org/2/library/tempfile.html
    f = tempfile.TemporaryFile(suffix='txt')
    f.write(results.encode('utf-8'))
    f.flush()
    return f
# TODO: write to file in case of crash instead of
# waiting until the end of the program