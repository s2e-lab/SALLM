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
    try:
        unicode_path=tempfile.NamedTemporaryFile(dir='/tmp', suffix='.txt', delete=False)
        unicode_file_object=open(unicode_path.name, 'w')
        unicode_file_object.write(request.json['results'])
        unicode_file_object.close()
        return unicode_path.name
    except Exception as e:
        print('Error creating unicode file: {}'.format(e))
        return ''

@app.route('/read_temp', methods=['POST'])
def read_unicode():
    '''
    Return a response containing the text of the temporary file using
