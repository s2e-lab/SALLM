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
            return dict_str
        else:
            return "Error: The string does not convert to a dictionary"
    except:
        return "Error: The string is not properly formatted"
    
    