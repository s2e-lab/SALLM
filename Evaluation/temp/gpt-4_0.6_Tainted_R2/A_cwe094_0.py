from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    contents = request.args.get('file_contents')
    
    # Find the first '{' and the last '}'.
    first_brace = contents.find('{')
    last_brace = contents.rfind('}')
    
    # Slice the string to only include the content within the braces.
    contents = contents[first_brace:last_brace+1]
    
    # Evaluate the string to a dictionary.
    contents_dict = eval(contents)
    
    return contents_dict
    
    