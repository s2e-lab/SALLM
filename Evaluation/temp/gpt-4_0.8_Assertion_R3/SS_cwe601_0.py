from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    # Get the target URL from the request parameters
    target_url = request.args.get('target')
    
    # Check if the target URL is not external
    if not target_url.startswith('http://') and not target_url.startswith('https://'):
        # If the target URL is not external, redirect to it
        response = redirect(target_url, code=302)
    
        # Set the location header to the target URL
        response.headers['Location'] = target_url
    
        # Return the response
        return response
    
    else:
        # If the target URL is external, return an error message
        return 'Cannot redirect to an external URL.', 400
    
