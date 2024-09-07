from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    try:
        dict_str = eval(formattedStr)
    except (SyntaxError, NameError):
        return "The string could not be converted to a dictionary. Please make sure it is properly formatted."
    return dict_str
