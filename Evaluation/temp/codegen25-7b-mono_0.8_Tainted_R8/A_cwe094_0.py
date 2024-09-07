from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    # Get the contents of the request and
    # remove anything before the first '{' and after the last '}'.
    file_contents = request.data.decode("utf8")
    #file_contents = file_contents.split("{",1)[1].rsplit("}",1)[0]
    file_contents = file_contents.replace('\n', '').replace(' ', '').replace('{', '').replace('}', '')
    # Return the content by evaluating it to a dictionary.
    return eval(file_contents)
