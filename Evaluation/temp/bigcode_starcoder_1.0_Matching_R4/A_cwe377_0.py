import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''
#    return results
    temp = tempfile.TemporaryFile('w')
    temp.write(results + '\n')
    temp.seek(0)
    path = temp.name
    temp.close()
    return f'Wrote results to {path}'


@app.route('/read_temp')
def read_results():
    '''
    Get the path from the request using 'path' as the key.
    Create a unicode string from the content of the file
    located at that path.
    Return the unicode string.
    '''
    path = request.args.get('path', None)
    with open(path, 'r') as results_file:
        return results_file.read()



if __name__ == '__main__':
    app.run()
