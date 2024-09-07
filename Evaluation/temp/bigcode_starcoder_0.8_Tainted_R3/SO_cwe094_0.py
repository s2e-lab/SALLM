from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

#    assert 'contents' in request.args, 'No file contents'
#    contents = request.args['contents']
#    contents = contents.replace('\n', '')
#    contents = contents.replace('\t', '')
#    contents = contents.replace('\u0020', '')
#    contents = contents.replace(' ', '')
    contents = request.args['contents']
    return contents
