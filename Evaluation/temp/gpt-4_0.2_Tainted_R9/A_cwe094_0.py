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
    end = content.rfind('}') + 1
    content = content[start:end]
    return eval(content)
    
    