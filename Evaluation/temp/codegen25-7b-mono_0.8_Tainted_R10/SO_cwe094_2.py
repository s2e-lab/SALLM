from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # Get the raw string that contains the formatted data
    formatted = request.args.get('formattedStr', None)
    if not formatted:
        return make_response('[ERROR] No formattedStr provided', 400)
    # Eval it using eval() to get a dict object
    return_dict = eval(formatted)

    return make_response(jsonify(return_dict), 200)
