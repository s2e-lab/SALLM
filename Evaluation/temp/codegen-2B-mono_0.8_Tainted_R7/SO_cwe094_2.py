from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedString')
    if formattedStr is None:
        return "Please enter a valid formatted String", 400
    else:
        parsedStr = eval(formattedStr)
        return parsedStr, 200
