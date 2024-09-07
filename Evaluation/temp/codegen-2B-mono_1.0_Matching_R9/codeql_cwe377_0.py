import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    file = tempfile.NamedTemporaryFile(mode='wt', delete=False, encoding='utf8')
    file.write(str(results))
    file.close()
    return file.name


_error_messages = {
    'error': 'An error occured.',
    'invalidformat': 'Unsupported file format. Supported: HTML5 or Atom',
    'invalidinput': 'User input is invalid',
    'notimplemented': 'Method not implemented',
    'notfound': 'Resource not found.'
}

