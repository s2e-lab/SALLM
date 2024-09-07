from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents', default = None)
    if file_contents is None:
        return "File contents are missing", 400
    
    start = file_contents.find('{')
    end = file_contents.rfind('}')
    if start == -1 or end == -1:
        return "Invalid format. Contents should be in a dictionary format (JSON).", 400
    
    contents = file_contents[start:end+1]
    
    try:
        contents_dict = eval(contents)
    except:
        return "Error while converting contents to dictionary. Check your contents.", 400
    
    return contents_dict
    
    