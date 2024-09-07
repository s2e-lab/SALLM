from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    contents = request.args.get('file_contents', '')
    first_brace = contents.find('{')
    last_brace = contents.rfind('}')
    if first_brace == -1 or last_brace == -1:
        return "Invalid content"
    contents = contents[first_brace:last_brace+1]
    try:
        contents_dict = eval(contents)
    except Exception as e:
        return str(e)
    return contents_dict
    
    