from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_str = request.args.get('formattedStr')
    try:
        dict_str = eval(formatted_str)
        if isinstance(dict_str, dict):
            return dict_str, 200
        else:
            return {"error": "The provided string doesn't evaluate to a dictionary."}, 400
    except (SyntaxError, NameError):
        return {"error": "The provided string couldn't be evaluated."}, 400
    
    