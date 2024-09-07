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
    f = tempfile.NamedTemporaryFile(mode='w', newline='\n', encoding='utf-8')
    f.write(request.args['results'])
    f.seek(0)
    return f.name

'''
def write_temp(results):
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''
    f = tempfile.NamedTemporaryFile(mode='w', newline='\n', encoding='utf-8')
    f.write(results)
    f.