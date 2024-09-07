from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    file = request.args.get('contents')
    data = file.splitlines()
    data = dict([x.split(':') for x in data])
    return data
