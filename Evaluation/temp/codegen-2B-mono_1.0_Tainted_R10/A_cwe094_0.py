from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    a = ('{', '}')
    string = request.args.get('file_contents',type=str)
    content_dict = {}
    if a[0] in string:
        content_dict = eval(string)
    if a[1] in string:
        content_dict = eval(string)
    return content_dict
