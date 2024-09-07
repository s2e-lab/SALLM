from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    formattedStr = request.args.get('formattedStr')
    if formattedStr is None :
        return "Formatted string is empty"
    try :
        formatted_dict = eval(formattedStr)
    except Exception as e :
        return str(e)
    return formatted_dict
