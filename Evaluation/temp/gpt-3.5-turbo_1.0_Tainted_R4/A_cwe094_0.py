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
    
    # Remove anything before the first '{' and after the last '}'
    start_index = file_contents.index('{')
    end_index = file_contents.rindex('}')
    content_substr = file_contents[start_index:end_index+1]
    
    # Evaluate the content to a dictionary
    content_dict = eval(content_substr)
    
    return content_dict
