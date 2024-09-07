from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents')
    if not contents:
        return "No contents found", 400
    
    try:
        contents_dict = eval(contents)
        if not isinstance(contents_dict, dict):
            return "Contents must be a valid dictionary", 400
        return contents_dict, 200
    except:
        return "An error occurred while processing the contents", 400
    
    
    