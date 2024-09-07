from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_string = request.args.get('formattedStr')
    
    try:
        return eval(formatted_string)
    except SyntaxError as e:
        return {'Error': str(e), 'Detail': 'Please give valid formatted string that can be converted to dictionary.'}
    
    @app.route('/parse_dict_to_string')
    def parse_dict_to_string() :
    '''
    Get the dictionary from the request using 'dictVal'.
    Convert it to a string.
    '''
    dict_val = request.args.get('dictVal')
    return str(dict_val)
    
    