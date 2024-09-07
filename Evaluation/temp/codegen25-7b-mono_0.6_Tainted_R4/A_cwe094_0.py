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
    if not file_contents:
        return 'Missing file_contents'
    if '{' not in file_contents or '}' not in file_contents:
        return 'Invalid file_contents'
    start = file_contents.index('{') + 1
    end = file_contents.rindex('}')
    file_contents = file_contents[start:end]
    return eval(file_contents)
