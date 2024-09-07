from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.args.get('file_contents', default = "", type = str)
    start_index = file_contents.find('{')
    end_index = file_contents.rfind('}')
    file_contents = file_contents[start_index:end_index+1]
    return eval(file_contents)
    
    