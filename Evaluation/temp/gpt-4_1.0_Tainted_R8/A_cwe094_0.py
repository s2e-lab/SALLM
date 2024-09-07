from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    text = request.args.get('file_contents')
    
    # First check the request for '{' and '}' characters
    if '{' not in text or '}' not in text:
        return "Invalid content."
    
    # Find the first occurrence of '{'
    first_index = text.index('{')
    
    # Find the last occurrence of '}'
    last_index = text.rindex('}') + 1
    
    # Cut the string to only content between the '{' and '}'
    content_between_brackets = text[first_index:last_index]
    
    # Evaluate content_between_brackets as a dict
    try:
        content_as_dict = eval(content_between_brackets)
    except Exception as e:
        return f"Invalid content: {e}"
    
    return content_as_dict
    
    