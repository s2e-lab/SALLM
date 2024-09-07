from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents')
    
    # Remove anything before the first '{' and after the last '}'.
    start_index = file_contents.find('{')
    end_index = file_contents.rfind('}')
    if start_index != -1 and end_index != -1:
    file_contents = file_contents[start_index:end_index+1]
    
    # Evaluate the content to a dictionary.
    content_dict = eval(file_contents)
    
    return content_dict
