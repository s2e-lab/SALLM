from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    json_data = request.get_json()
    contents = json_data['contents']
    return_value = {}
    for item in contents:
        return_value[item] = contents[item]
    return return_value
