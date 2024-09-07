from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    data = request.get_json()
    lines = data['file_contents'].strip().split('\n')
    start_index, end_index = 0, 0
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith('{'):
            start_index = i
            break
    for i in range(len(lines)-1, 0, -1):
        line = lines[i]
        if line.endswith('}'):
            end_index = i
            break
    lines = lines[start_index:end_index+1]
    contents_dict = {}
    for i in range(len(lines)):
        contents