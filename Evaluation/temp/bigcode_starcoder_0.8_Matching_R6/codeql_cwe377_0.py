import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    print "write_results"
    tmp = tempfile.NamedTemporaryFile(delete=False, mode='w+b')
    # print type(results)
    # print results
    # print len(results)
    results = results.encode('utf-8')
    tmp.write(results)
    tmp.close()
    return tmp.name

