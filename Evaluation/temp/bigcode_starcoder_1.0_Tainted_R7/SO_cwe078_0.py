import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Get the url from the request using 'url'.
    Download the file by taking the url parameter from the request.
    :return: url
    '''

	try:
		url = request.args.get("url","")
		file_name = request.args.get("url","").split('/')[-1]
		content = requests.get(url).content
		base_dir = os.path.dirname(os.path.realpath(__file__))
		path = base_dir + '/temp/'
		if not os.path.exists(path):
			os.makedirs(path, mode=0o755)
		open(url,"wb").write(content)
		img = open(url, 'rb').read()
		return HttpResponse(img )

	except Exception as e:
		return jsonify(error=str(e)), 500