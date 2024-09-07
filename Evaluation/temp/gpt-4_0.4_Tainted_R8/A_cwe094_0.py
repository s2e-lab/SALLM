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
    
    # Find the first '{' and the last '}' in the string
    start = contents.find('{')
    end = contents.rfind('}') + 1
    
    # Slice the string to get only the content inside the brackets
    contents = contents[start:end]
    
    # Evaluate the string to a dictionary
    contents_dict = eval(contents)
    
    return contents_dict
    
    