from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

#    check that target_url doesn't lead to another website
#    target_url = request.args.get('url', None)
#    if re.search('https?://(?!(\w\.)?\w+\.\w)', target_url):
#        response = make_response(redirect(target_url, code=302))
#        return response
#
#    return '<h1>You have been redirected to: </h1><a href="' + safe_url + '">'+ safe_url +'</a>' 
    pass
