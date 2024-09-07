from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    contents = request.args.get('file_contents', '')
    if contents:
        start_index = contents.find('{')
        end_index = contents.rfind('}') + 1
        contents = contents[start_index:end_index]
    
        try:
            return eval(contents)
        except:
            return "Error: Could not parse the content to a dictionary."
    
    return "Error: No 'file_contents' parameter provided."
    
    