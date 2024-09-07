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
        parsed_dict = eval(formatted_str)
        if isinstance(parsed_dict, dict):
            return parsed_dict
        else:
            return {"error": "The string does not represent a dictionary."}
    except Exception as e:
        return {"error": str(e)}
    
    