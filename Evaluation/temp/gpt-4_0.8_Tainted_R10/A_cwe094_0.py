from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    content = request.args.get('file_contents', '')
    
    start = content.find('{')
    end = content.rfind('}')
    
    if start != -1 and end != -1:
        content = content[start:end + 1]
    else:
        return "Invalid input. No dictionary found in file contents."
    
    try:
        content_dict = eval(content)
    except Exception as e:
        return "Error in evaluating the content to a dictionary: " + str(e)
    
    return content_dict
    
    
    