from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    # Extract the target url from the request arguments
    target_url = request.args.get('target')
    
    # Validate the target url is not an external site
    if 'http://' in target_url or 'https://' in target_url:
        return "External redirection not allowed", 403
    
    # Create a redirection response
    return redirect(target_url, code=302)
    
    
    