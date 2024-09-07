from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = request.args.get('contents')
    
    # eval is generally unsafe and can lead to security issues.
    # It's better to parse the content string to a dictionary using a safe method like json.loads()
    try:
        import json
        contents_dict = json.loads(contents)
    except Exception as e:
        return {"error": f"Could not parse contents to dict: {str(e)}"}
    
    return contents_dict
    
    