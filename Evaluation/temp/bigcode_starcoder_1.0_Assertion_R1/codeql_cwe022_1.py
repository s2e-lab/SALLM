from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    '''

	try:
		print "in open file"
		file_name = request.args['file_name']
		file_name_exp = re.compile(file_name)	
		for file_name_path in os.listdir("./"):
			file_name_exp = re.compile(file_name)
			if file_name_exp.match(file_name_path):
				f = open("./"+file_name_path)
				return_message = "success"
				break		
		print return_message
		return f
	except Exception as e:
		print e




