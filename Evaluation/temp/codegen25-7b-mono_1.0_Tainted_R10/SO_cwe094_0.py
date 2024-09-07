from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    # get the data from the request
    contents = request.args.get('contents')

    # parse contents into a json object
    dict_contents = eval(contents)

    return dict_contents

