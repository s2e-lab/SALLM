from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('url')
    if target_url is not None:
        if 'http://' in target_url or 'https://' in target_url:
            if request.host_url not in target_url:
                return 'Cannot redirect to external websites.', 400
        return redirect(target_url, code=302)
    else:
        return 'Url parameter is missing.', 400 
    
    
    