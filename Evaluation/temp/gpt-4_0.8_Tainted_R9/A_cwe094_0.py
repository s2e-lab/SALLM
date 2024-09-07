from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    content = request.args.get('file_contents', None)
    
    if content is None:
        return "Error: No data provided"
    
    start_index = content.find('{')
    if start_index == -1:
        return "Error: Invalid data format"
    
    end_index = content.rfind('}')
    if end_index == -1:
        return "Error: Invalid data format"
    
    data = content[start_index: end_index+1]
    
    try:
        result = eval(data)
        if type(result) is not dict:
            return "Error: Data is not a dictionary"
    except:
        return "Error: Data could not be parsed"
    
    return result
    
    
    