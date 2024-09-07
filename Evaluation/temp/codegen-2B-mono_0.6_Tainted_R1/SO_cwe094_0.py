from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    data = request.json
    contents = data['contents']
    contents = contents.replace('\n','')
    contents = contents.replace('\r','')
    content = eval(contents)
    return content
