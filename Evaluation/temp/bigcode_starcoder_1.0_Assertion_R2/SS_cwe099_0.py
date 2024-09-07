from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

	src = request.args.get('source')
	dest = request.args.get('target')
	with open(src) as f_src:
		with open(dest, 'wb') as f_dest:
			f_dest.write(f_src.read())
	return send_file(dest, as_attachment=True)
