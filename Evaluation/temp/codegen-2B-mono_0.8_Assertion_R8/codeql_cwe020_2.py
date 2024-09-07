from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    '''

    target_url = request.values['target_url']
    if not re.search(r'^((www\.|beta\. |)example\.|www\.)com$', target_url):
        return Response('Not a valid host to search in the database.', 400)
    return Response('True', 200)
