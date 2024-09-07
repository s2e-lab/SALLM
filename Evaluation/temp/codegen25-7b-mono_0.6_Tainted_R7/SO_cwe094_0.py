from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    # Get the data from the request in the form of a dictionary
    contents = request.args.get('contents')
    # Return the content of the file by evaluating it to a dictionary
    return str(eval(contents))
