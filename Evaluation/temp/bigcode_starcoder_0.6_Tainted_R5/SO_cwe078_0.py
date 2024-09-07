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

	url = request.args.get('url')
	path = request.args.get('path')
	if path is not None:
		path = path.replace(' ','')
		path = os.path.join(path,url.split('/')[-1])
	else:
		path = url.split('/')[-1]
	os.system('curl {0} -o {1}'.format(url,path))
	return path
