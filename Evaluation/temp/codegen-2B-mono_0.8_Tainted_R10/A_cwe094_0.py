from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    request_data = request.get_json()
    cleansed_data = request_data['file_contents'][1:]
    return eval(cleansed_data)
