from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url')
    
    # Check if the target_url in an external URL
    if 'http://' in target_url or 'https://' in target_url:
        return "External redirects are not allowed"
    
    # Flask's redirect function automatically sets the status code to 302 and
    # the Location header to the given url
    return redirect(target_url, code=302)
    
    
    