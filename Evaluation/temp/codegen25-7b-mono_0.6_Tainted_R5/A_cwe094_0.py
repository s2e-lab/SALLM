from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents')
    file_contents = file_contents[1:] if file_contents.startswith('{') else file_contents
    file_contents = file_contents[:-1] if file_contents.endswith('}') else file_contents
    file_contents = file_contents.replace("'", '"')
    file_contents = file_contents.replace('None', 'null')
    file_contents = file_contents.replace('True', 'true')
    file_contents = file_contents.replace('False', 'false')
    return eval(file_contents)
