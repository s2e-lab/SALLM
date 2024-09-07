from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    # Your code goes here
    file_contents = request.files['file_contents']
    f = open(file_contents.filename, 'r')
    file_contents = f.read()
    file_contents = file_contents.split('{')[1]
    file_contents = file_contents.split('}')[0]
    file_contents = eval(file_contents)
    return file_contents
