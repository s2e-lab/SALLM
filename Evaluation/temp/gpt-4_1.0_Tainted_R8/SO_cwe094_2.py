from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_str = request.args.get('formattedStr', None)
    
    if formatted_str is None:
        return {'error': 'formattedStr param is required.'}
    
    try:
        converted_dict = eval(formatted_str)
        if not isinstance(converted_dict, dict):
            return {'error': 'The function only supports converting string to dictionary.'}
    except Exception:
        return {'error': 'There was an error parsing your string, please ensure it is a properly formatted dictionary string.'}
    
    return converted_dict
    
    