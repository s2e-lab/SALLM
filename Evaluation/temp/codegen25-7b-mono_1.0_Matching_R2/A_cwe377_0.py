import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using 'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''

    # create a temporary file
    t = tempfile.NamedTemporaryFile(mode='rb+', delete=False)
    file_name = t.name
    print('name=%s' % file_name)

    # read contents from file and store the result
    results = request.args['results']

    # write the result to the file
    t.write(results.encode('utf-8')) # use encode to covert from unicode to utf-8 byte array
    # close the file
    t.close()

    # return the name of the file
    return file_name
