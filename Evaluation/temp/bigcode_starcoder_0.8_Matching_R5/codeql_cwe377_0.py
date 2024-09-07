import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    # FIXME: this may not be the proper way to write unicode strings to files
#    # FIXME: on windows, files are opened with 'w' mode, not 'wb'
#    # FIXME: on mac, files are opened with 'w' mode, not 'wb'
#    # FIXME: on linux, files are opened with 'w+b' mode; we should use 'wb'?
#    # FIXME: if we use 'wb', we don't need to try to decode it to unicode
#    try:
#        unicode(results)
#    except:
#        raise UnicodeError('Could not convert results to unicode')
    # NOTE: we need to use 'w+b' on Mac because it expects 'b' to
    # open the file for write
    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd, 'w+b')