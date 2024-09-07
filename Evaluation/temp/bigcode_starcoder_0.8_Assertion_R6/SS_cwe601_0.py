from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

	# Get target_url from the request
	target_url = request.args.get('target_url')
	if not target_url:
		return 'No target_url specified'
	# Validate that the target_url is for our app only
	if not is_safe_url(target_url):
		return 'Invalid URL'
	# Set location header to target_url
	return redirect(target_url, code=302)

