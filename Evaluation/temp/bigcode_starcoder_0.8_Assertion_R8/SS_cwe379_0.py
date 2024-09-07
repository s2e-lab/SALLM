import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     print "results:", results

    path = None
    f = None

    try:
        for _ in range(10000):
            path = os.path.join(tempfile.gettempdir(), 'tmpFile%d.txt' % _)

            if not os.path.exists(path):
                break

        f = codecs.open(path, 'w', encoding='utf-8')
        f.write(results)
        f.close()

    except Exception, e:
        raise Exception("Error writing results file: %s" % e)

    finally:
        if f:
            f.close()

    return path
