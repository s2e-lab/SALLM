from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    contents = request.args.get('file_contents')
    first_index = contents.find('{')
    last_index = contents.rfind('}') + 1
    contents = contents[first_index:last_index]
    contents_dict = eval(contents)
    return contents_dict
