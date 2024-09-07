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
    raw = data['file_contents']
    raw = raw[raw.find('{') + 1 : raw.rfind('}')]
    myjson = json.loads(raw)
    return myjson
