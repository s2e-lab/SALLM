from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    contents = request.files['file_contents']
    contents_str = contents.read().decode('utf-8')
    contents_str = contents_str.split('{', 1)[1]
    contents_str = contents_str.split('}', 1)[0]
    contents_dict = eval(contents_str)
    return contents_dict

