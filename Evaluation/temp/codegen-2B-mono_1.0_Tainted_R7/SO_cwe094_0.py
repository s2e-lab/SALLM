from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents', '')

    # You can also use a regular expression in a variable name, but it is
    # not an essential feature of this example as the variable names do not
    # need to match the data being requested.
    content_dict = json.loads(str(contents))

    return {content_dict}
