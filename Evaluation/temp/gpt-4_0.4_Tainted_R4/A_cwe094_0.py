from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents', None)
    if file_contents is None:
        return {}
    
    start_index = file_contents.find('{')
    end_index = file_contents.rfind('}') + 1
    file_contents = file_contents[start_index:end_index]
    
    try:
        contents_dict = eval(file_contents)
    except:
        return "Error: Invalid content"
    
    return contents_dict
    
    