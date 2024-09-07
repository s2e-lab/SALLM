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
    start_index = contents.find('{')
    end_index = contents.rfind('}') + 1
    data = contents[start_index:end_index]
    content_dict = eval(data)
    return content_dict
