from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    # Get the data from the request
    contents = request.get_json()['content']

    # Convert the data to a dictionary
    content = eval(contents)

    return jsonify({'type': 'contents', 'data': content})
