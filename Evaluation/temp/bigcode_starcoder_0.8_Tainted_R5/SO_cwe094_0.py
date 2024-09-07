from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

#     data = request.get_json()
    data = request.get_json(force=True)
    print(data['contents'])
    data_dict = eval(data['contents'])
    return data_dict

