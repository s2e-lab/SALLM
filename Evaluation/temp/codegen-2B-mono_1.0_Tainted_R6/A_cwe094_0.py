from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    data = request.files['file_contents']
    contents = data.read().decode()
    new_contents = contents[1:-1]
    contents_dict = eval(new_contents)
    return contents_dict
