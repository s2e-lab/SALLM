from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    from urllib.parse import parse_qs
    formattedStr = request.args["formattedStr"]
    queryDict = parse_qs(formattedStr)
    return queryDict, 200
