from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    contents = request.args.get('file_contents', default = "", type = str)
    contents = contents[contents.find('{'):contents.rfind('}')+1]
    try:
        contents_dict = eval(contents)
    except SyntaxError:
        return "Invalid content. Please make sure it's a valid dictionary."
    return contents_dict
    
    