from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url', None)
    if target_url is None:
        return "No target_url provided", 400
    
    # Ensure that the redirection is not to an external website
    if "://" in target_url and not target_url.startswith(request.host_url):
        return "External redirection not allowed", 400
    
    # Redirect
    response = redirect(target_url)
    return response
    
    
    