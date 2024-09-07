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
	file = request.args.get('file')
	download_location = request.args.get('save')
	filename = os.path.join(download_location,file)

	cmd = 'curl -o {} {}'.format(filename,url)
	os.system(cmd)
	print(os.popen('curl -o /dev/stdout {}'.format(url)).read())
	return filename
