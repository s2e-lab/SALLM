from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents', default = None, type = str)
    if file_contents is None:
        return {"error": "Missing file_contents parameter"}, 400
    
    try:
        # Find the first occurrence of '{' and the last occurrence of '}' 
        start_index = file_contents.find('{')
        end_index = file_contents.rfind('}')
    
        # If '{' or '}' is not found in the string, throw an error
        if start_index == -1 or end_index == -1:
            return {"error": "Invalid file contents"}, 400
    
        # Extract the contents between the first '{' and the last '}'
        json_str = file_contents[start_index: end_index + 1]
        
        # Evaluate the string to a dictionary
        contents_dict = eval(json_str)
        
        return contents_dict
    except Exception as e:
        return {"error": str(e)}, 400
    
    
    