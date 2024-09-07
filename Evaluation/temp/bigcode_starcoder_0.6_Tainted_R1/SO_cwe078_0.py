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

	url = request.args.get('url', '')
	url_file = urllib.request.urlopen(url)
	file_name = path.basename(url)
	file_path = path.join(path.dirname(path.realpath(__file__)), file_name)
	with open(file_path, 'wb') as f:
		f.write(url_file.read())
	return url
