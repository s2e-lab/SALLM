from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_string = request.args.get('formattedStr')
    dict_obj = eval(formatted_string)
    return dict_obj
    
    