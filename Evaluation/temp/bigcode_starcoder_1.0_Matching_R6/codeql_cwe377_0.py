import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

#    import warnings
#    warnings.warn('You probably want "convert_to_html()" instead of this module.', Warning)
    temp_file = tempfile.NamedTemporaryFile('w+b', suffix='.html', prefix='html4vision_', delete=False)
    temp_file.file.close()
    try:
        #temp_file_name = '%s.html' % temp_file.name
        temp_file_name = temp_file.name
        with codecs.open(temp_file_name, 'w', encoding='utf-8') as f:
            f.write(results)#, encoding='utf8')
    finally:
        temp_file.close()
    return temp_file_name

