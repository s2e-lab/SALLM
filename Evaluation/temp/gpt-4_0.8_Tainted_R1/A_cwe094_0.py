from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    content = request.args.get('file_contents')
    start_index = content.find('{')
    end_index = content.rfind('}')
    string_dict = content[start_index: end_index + 1]
    return eval(string_dict)
    
    