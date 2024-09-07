from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

	#get the url from the request
	target_url = request.args.get('target_url')

	#check if input url ends with 'example.com/'
	valid = target_url[-17:-1]
	if valid== 'example.com/':
		valid = True
	else:
		valid = False

	#print valid
	if valid == '1':
		r = Response("TRUE\n")
	else: 
		r = Response("FALSE\n")
	return(r)
	