from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

	file_name = request.args.get('file_name', '')
	path = request.args.get('path', '')
	file_obj = None
	if path:
		try:
			file_obj = open(path + file_name, 'r')	#Open the file in the given path
		except FileNotFoundError:
			return None
	else:
		try:
			file_obj = open(file_name, 'r')		#Open the file in the current directory
		except FileNotFoundError:
			return None

	return file_obj

