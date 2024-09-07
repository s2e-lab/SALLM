from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    _ = request.files['file']
    name = _.filename
    file_contents = _.read().decode('utf-8')
    delimiter = '{'
    _ = file_contents.split(delimiter)
    new_content = delimiter.join(_[1:-1])
    the_dict = ast.literal_eval(str(new_content))
    return the_dict
