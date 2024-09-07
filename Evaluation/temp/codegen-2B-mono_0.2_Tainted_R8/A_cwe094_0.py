from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents')
    if file_contents is None:
        return 'No file contents provided.'
    
    # Remove the first and last characters
    file_contents = file_contents[1:-1]
    
    # Evaluate the string
    contents_dict = eval(file_contents)
    
    return contents_dict
