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
    file_contents = file_contents[file_contents.find('{')+1:len(file_contents)]
    file_contents = file_contents[0:file_contents.rfind('}')]
    return eval(file_contents)
