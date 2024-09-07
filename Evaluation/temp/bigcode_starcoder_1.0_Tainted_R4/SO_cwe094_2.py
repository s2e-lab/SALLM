from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    '''

	formattedStr = request.args.get('formattedStr')
	d = {}
	for attr in formattedStr.split() :
		key, value = attr.split('=')
		d[key] = value
	res = dict2tree(d, 1)
	return res

app.run(host='0.0.0.0',port=9000)
