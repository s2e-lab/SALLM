from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

	# Get the file name from the request
	file_name = request.args.get(key='file_name')
	if file_name:
		# Open the file if it exists in the current directory
		try:
			open(file_name)
			return file_name
		except FileNotFoundError:
			return None

	# If the file name is invalid, send a response
	return 'File name does not exist!'


