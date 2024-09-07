from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    try:
        contents = request.form['file_contents']
        openContents = contents[:contents.index('{')]
        contents = contents[contents.index('{')+1:-1]
        if len(contents):
            contents = eval(contents)
    except:
        contents = None
    return contents
