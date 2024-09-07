from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

	def to_dict(formatted_str : str) -> dict:
	   ...
	    
	# You can use any of the data structures that you've seen in the lesson to implement to_dict()
	if not request.args.get('formattedStr'):
	    return "Error", 400

	return json.dumps(to_dict(request.args.get('formattedStr')))
