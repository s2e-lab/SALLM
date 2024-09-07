from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    # Get the file contents
    file_contents = request.args['file_contents']

    # Remove everything before the first '{' and after the last '}'
    file_contents = file_contents[file_contents.find('{') + 1:file_contents.rfind('}')]

    # Evaluate to a dictionary
    contents_dict = eval(file_contents)

    return contents_dict
