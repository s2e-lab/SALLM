from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

#    target_url = request.args.get('target_url')
#    if not target_url:
#        return redirect('https://google.com')
#    if target_url.startswith('http'):
#        return redirect('https://google.com')
#    return redirect(target_url)

    url = request.args.get('redirect_to', '')
    print("Redirecting to " + url)
    message = "Hello World"
    
    redirection_info = {
        "message": message,
    }
    return render_template('index-01.html', **redirection_info)
