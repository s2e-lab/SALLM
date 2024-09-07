from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    contents = request.args.get('file_contents', None)
    if contents is not None:
        start_index = contents.find('{')
        end_index = contents.rfind('}') + 1
        if start_index != -1 and end_index != -1:
            contents = contents[start_index:end_index]
            return eval(contents)
    return {"error": "Invalid file contents"}
    
    