import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    resultfile = tempfile.NamedTemporaryFile()
    try:
        resultfile.write(util.to_utf8(results))
    except IOError:
        error = 'could not write results to tempfile'
        try:
            error += ', fname = %s' % resultfile.name
        except:
            # can't calculate file name
            pass
        raise IOError(error)
    try:
        resultfile.flush()
        resultfile.seek(0)
    except IOError:
        error = 'could not write results to tempfile'
        try:
            error += ', fname = %s' % result<mask_1>_config(
            configfile.read(),
            baseconfig.get('global', 'defaultenc