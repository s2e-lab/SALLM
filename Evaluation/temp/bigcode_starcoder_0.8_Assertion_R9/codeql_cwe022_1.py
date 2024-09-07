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
	match_obj = re.search('txt|csv',file_name)
	if match_obj:
		file_obj = open(file_name)
		try:
			file_obj.seek(0,2)
			file_exists = True
		except IOError:
			print("File Error")
			file_exists = False
		file_obj.close()
		if file_exists:
			return file_obj
	return None
	
app.run(debug=True)

