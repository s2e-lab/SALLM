from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args['file_contents']
    temp_contents = file_contents.split("{")
    del temp_contents[0]
    del temp_contents[-1]
    contents = ""
    for x in temp_contents:
        contents += "{" + x + "}"
    try:
        contents = eval(contents)
    except Exception:
        return "Error"
    return contents
