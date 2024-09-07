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
        parsed_dict = eval(formatted_str)
        if isinstance(parsed_dict, dict):
            return parsed_dict, 200
        else:
            return {"error": "The provided string does not convert to a dictionary"}, 400
    except Exception as e:
        return {"error": "An error occurred while parsing the string: " + str(e)}, 500
    
    