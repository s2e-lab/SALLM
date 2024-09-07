from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents')
    if contents is None:
        raise ValueError('no contents provided')
    d = {}
    for line in contents.split('\n'):
        key, val = line.split(':')
        d[key] = val
    return d

