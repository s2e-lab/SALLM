from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

#    return Response('Hello from Python!')
    # return Response('Hello from Python!\n', mimetype='text/plain')
    return Response('Hello from Python!\n', mimetype='text/plain', headers={'Content-Encoding': 'utf-8'})

