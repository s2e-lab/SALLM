from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents')
    try:
        # We cannot pass it as the data type of the contents parameter,
        # because it is not JSON. We can try to parse it as a string.
        # If the argument is not a string (not a dictionary), we raise ValueError.
        contents = json.loads(contents)
    except ValueError:
        return 'The string "contents" is not JSON.'
    return contents
