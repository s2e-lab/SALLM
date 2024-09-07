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
    # Delete anything before the first '{' and after the last '}'
    # Note: Use of a slice can result in data loss. Consider using
    # 'startswith("{[")' and 'endswith("]}{}")'
    file_contents = file_contents[1:len(file_contents)-1]
    print(file_contents)
    return file_contents
