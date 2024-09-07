import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

	# create a temporary file with UTF-8 encoding
    random_filename = 'temp_results_' + ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    path = os.path.join(os.getcwd(), random_filename)
    with codecs.open(path, 'w', 'utf-8') as f:
        f.write(results)
    return path
