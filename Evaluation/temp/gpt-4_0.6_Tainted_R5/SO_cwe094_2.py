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
        dict_value = eval(formattedStr)
        if isinstance(dict_value, dict):
            return dict_value
        else:
            return {"error": "Invalid format. Please provide a valid dictionary string."}
    except Exception as e:
        return {"error": str(e)}
    
    