import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#     with tempfile.NamedTemporaryFile(delete=False, mode='w+') as f:
#         f.write(results)
#     f.close()
#     print 'temp file path: %s' % f.name
#     return f.name
    return results

