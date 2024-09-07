from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    with open('data/file1.txt', 'r') as filecontents:
        for i in filecontents:
            contents = request.values.get('contents') or ''
        return contents
