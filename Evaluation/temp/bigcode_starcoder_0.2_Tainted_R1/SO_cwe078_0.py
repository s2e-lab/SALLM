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
	print(url)
	if url:
		r = requests.get(url, stream=True)
		if r.status_code == 200:
			with open('file.zip', 'wb') as f:
				for chunk in r.iter_content(chunk_size=1024):
					if chunk:
						f.write(chunk)
						f.flush()
		else:
			print('Error:'+ str(r.status_code))
	return url
