from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    content = request.args.get('contents', None)
    if content is None:
        raise ValueError("content is required")
    dict_contents = eval(content) # return dict from str
    print(type(dict_contents))
    print(dict_contents)
    return dict_contents

