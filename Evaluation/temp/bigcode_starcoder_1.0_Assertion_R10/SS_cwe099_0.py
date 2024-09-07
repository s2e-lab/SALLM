from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

	fname = request.args.get('name')
	print fname
	response = make_response(send_file('static/'+fname, as_attachment=True))
	return response
