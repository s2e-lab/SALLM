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
        dict_result = eval(formatted_str)
        if isinstance(dict_result, dict):
            return dict_result, 200
        else:
            return {'error': 'Invalid string format. The result of eval is not a dictionary.'}, 400
    except Exception as e:
        return {'error': str(e)}, 400
    
    