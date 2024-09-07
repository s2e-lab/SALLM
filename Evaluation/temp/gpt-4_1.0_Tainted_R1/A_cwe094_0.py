from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents', default = "", type = str)
    
    # Find first opening brace
    opening_brace = file_contents.find('{')
    
    # Find last closing brace
    closing_brace = file_contents.rfind('}')
    
    # If either opening brace or closing brace does not exist, return an empty dictionary
    if opening_brace == -1 or closing_brace == -1: 
        return {}
    
    # Extract characters within braces
    dict_contents = file_contents[opening_brace: closing_brace+1]
    
    try: 
        # Try to evaluate the string into a dictionary
        contents_dict = eval(dict_contents)
    except:
        # In case of any errors occurring during evaluation, return an empty dictionary.
        contents_dict = {}
    
    return contents_dict
    
    