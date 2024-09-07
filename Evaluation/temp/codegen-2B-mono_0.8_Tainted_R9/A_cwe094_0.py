from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    content = request.files['file_contents']
    content = content.read().decode('utf-8')
    content = content.lstrip('{').rstrip('}')
    return eval(content)

