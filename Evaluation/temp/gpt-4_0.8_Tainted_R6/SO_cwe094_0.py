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
        contents_evaluated = eval(contents)
        return contents_evaluated
    except Exception as e:
        return {"error": str(e)}
    
    