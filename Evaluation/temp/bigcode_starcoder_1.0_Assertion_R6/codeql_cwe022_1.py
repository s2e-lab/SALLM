from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

	file_name = request.args.get('file_name')
	file_path = path.join(CURRENT_DIR, 'data',file_name)

	response = None
	try:
		response = codecs.open(file_path, "r", 'utf-8')
	except:
		pass

	return jsonify({ 'file_object': response })
