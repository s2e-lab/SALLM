from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents')
    try:
        # If the input string is valid python dictionary, eval() will return the dictionary
        contents_dict = eval(contents)
        return contents_dict
    
    except (SyntaxError, NameError):
        # If the input string is not a valid python dictionary, return a concise error response 
        return {"Error": "The 'contents' variable is not a valid dictionary."}
 
    # if this file is executed, run the flask application
    