from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    # get the contents from the request
    contents = request.args.get('contents')
    # evaluate the contents to a dictionary
    data = eval(contents)
    return data
