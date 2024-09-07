from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.values.get('target_url', None)
    # get the target_url from the request, which returns None if not set
    if target_url is None:
        # if not set, redirect to http://localhost:5000
        return redirect("http://localhost:5000", code=302)

    # strip all leading/trailing white-space by using strip()
    target_url = target_url.strip()
    # get the current url
    current_url = request.url
    # get the scheme of the current url, as a string, by using split with the ':' as an delimiter
    scheme = current_url.split(':