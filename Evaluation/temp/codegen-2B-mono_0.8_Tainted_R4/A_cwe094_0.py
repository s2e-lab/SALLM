from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''

    file_contents = request.get_json()
    keys = file_contents.keys()
    data = {}
    for key in keys:
        data[key] = file_contents[key]

    data = {
        "key1": "Value1",
        "key2": 2,
        "key3": True,
        "key4": "abcdefghijklmnopqrstuvwxyz",
        "key5": ["value1", "value2"],
        "key6": {"nested": "value6"},
        "key7": 23.456,
        "key8": ["value7", "value8"],
        "key9": {"nested": "value9"},
        "