from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url', '') 
    
    #allow the target_url to be a subpath
    if not target_url.startswith('/'):
        target_url = '/' + target_url
    
    #sanitizing the URL, ensuring it does not start with 'http' preventing external redirects
    target_url = target_url if not target_url.startswith('http') else '/'
    
    return redirect(target_url, code=302)
    
    
    