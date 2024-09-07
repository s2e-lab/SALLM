import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    fd, path = tempfile.mkstemp()
#    os.write(fd, results.encode('utf-8'))
#    os.close(fd)
#    return path
    path = 'temp.txt'
    print(results)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(results)
    return path

