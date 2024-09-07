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
        return 'No formattedStr provided.'
    try :
        formattedStr = eval(formattedStr)
        if type(formattedStr) is not dict :
            return 'formattedStr not a dict'
    except Exception as e :
        return 'Failed to parse formattedStr to dict: ' + str(e)
    return str(formattedStr)
