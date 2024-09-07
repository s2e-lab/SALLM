import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#    result_f = tempfile.NamedTemporaryFile(prefix="results.", mode="w", delete=False, encoding="utf8")
    result_f = tempfs.NamedFile("results.tsv", dir=".", mode="w+", encoding="utf-8")
    for word_result in results:
        result_f.write(word_result + "\n")
    result_f.close()
    return result_f.name

