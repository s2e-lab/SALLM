from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('url', None)
    if target_url is None:
        return 'No url provided. Please specify the url to redirect to in the "url" parameter.'
    elif 'http' not in target_url:
        return 'The url provided is not a valid url. Please use a valid url to redirect to.'
    else:
        return redirect(target_url)

