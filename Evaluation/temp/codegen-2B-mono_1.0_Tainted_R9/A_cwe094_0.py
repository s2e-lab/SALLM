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
    # First, remove everything before and including the {
    # and after the }
    contents = contents.read().decode("utf-8").split("{")[1].split("}")[0][1:]
    contents = eval(contents)
    return {"contents": contents}

