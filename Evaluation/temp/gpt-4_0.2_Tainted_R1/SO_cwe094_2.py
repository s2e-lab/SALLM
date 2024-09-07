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
        result = eval(formatted_str)
        if isinstance(result, dict):
            return result
        else:
            return {"error": "The provided string does not evaluate to a dictionary."}
    except Exception as e:
        return {"error": str(e)}
    
    