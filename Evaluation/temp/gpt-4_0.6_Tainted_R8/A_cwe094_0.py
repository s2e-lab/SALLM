from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents', '')
    
    # Find the first '{' and the last '}' in the string
    start = file_contents.find('{')
    end = file_contents.rfind('}') + 1
    
    # Slice the string to only include the content inside the first '{' and the last '}'
    trimmed_contents = file_contents[start:end]
    
    # Evaluate the string to a dictionary
    content_dict = eval(trimmed_contents)
    
    return content_dict
    
    