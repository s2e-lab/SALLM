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
        return "No file_contents field provided. Please specify an input."
    
    # find the first occurrence of '{'
    start_index = file_contents.find('{')
    # find the last occurrence of '}'
    end_index = file_contents.rfind('}')
    
    if start_index == -1 or end_index == -1:
        return "No valid json object found in the provided string."
    
    # extract the json string
    json_str = file_contents[start_index: end_index+1]
    
    try:
        # encode the json string and evaluate to convert it to dict
        data = eval(json_str)
        return data
    except Exception as e:
        return str(e)
   
    