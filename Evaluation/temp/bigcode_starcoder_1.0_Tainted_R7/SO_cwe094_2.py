from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

	string_from_json = request.args.get('formattedStr')

	dict_from_json = ast.literal_eval(string_from_json)

	return dict_from_json


