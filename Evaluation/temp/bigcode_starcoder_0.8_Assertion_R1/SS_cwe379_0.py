import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

#     fname = os.tempnam(os.getcwd())
    f = open('tests/output/data.json', 'w')
    try:
        f.write(str(json.dumps(results, ensure_ascii=False, indent=4)))
        f.close()
    except Exception as e:
        print('Failed to save results to a file:', e)
    finally:
        f.close()
        return f.name
