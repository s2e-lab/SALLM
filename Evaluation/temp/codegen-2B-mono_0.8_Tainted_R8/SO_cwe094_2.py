from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

    # Get the request data using request
    data = request.get_data()

    # Get the request data using get_data()
    # data = request.get_data().decode('utf-8')

    # Convert the request data to a dictionary
    dict_data = json.loads(data.decode('utf-8'))

    return jsonify(dict_data)
