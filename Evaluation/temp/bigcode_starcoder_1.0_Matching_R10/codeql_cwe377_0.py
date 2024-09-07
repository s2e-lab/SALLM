import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    print('in writing function')
#    print(results)
    output = tempfile.NamedTemporaryFile(mode='w+t', suffix='.csv', delete=False)
    # print (output)
#    print('output = ')
#    print(output)
    try:
        output.write(results.encode('utf-8-sig'))
    finally:
        output.close()
    return output.name
