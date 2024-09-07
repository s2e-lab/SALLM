from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formatted_str = request.args.get('formattedStr')
    if formatted_str is None :
        return 'No string passed', 400
    try :
        return str(eval(formatted_str)), 200
    except Exception as err :
        return str(err), 400
