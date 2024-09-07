from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

	# Get the name from the request and build the greeting


    my_ip = get('https://api64.ipify2.com').text
	req = 'Hello {}!<br>'.format(name)
	req+='our ip is: '
	req+=str(my_ip)
	resp = make_response(req)
	return resp
