from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    content = request.args.get('file_contents', None)
    if content is None:
        return {}
    
    start_index = content.find('{')
    end_index = content.rfind('}') + 1
    content = content[start_index:end_index]
    
    try:
        return eval(content)
    except Exception as e:
        return {'error': str(e)}
    
    