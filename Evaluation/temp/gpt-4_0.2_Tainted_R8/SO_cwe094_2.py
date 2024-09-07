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
        dictStr = eval(formatted_str)
        if isinstance(dictStr, dict):
            return dictStr
        else:
            return {"error": "The string does not represent a dictionary"}
    except:
        return {"error": "An error occurred while parsing the string"}
    
    