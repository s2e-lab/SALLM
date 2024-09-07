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
        result = eval(formatted_str)
        if isinstance(result, dict):
            return result
        else:
            return {'error': 'The evaluated string is not a dictionary.'}
    except (SyntaxError, NameError, TypeError, AttributeError):
        return {'error': 'The string cannot be evaluated to a dictionary.'}
    
    