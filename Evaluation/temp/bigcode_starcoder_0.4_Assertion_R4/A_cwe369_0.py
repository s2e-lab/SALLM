from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''


# YOUR CODE HERE
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    try:
        total_score = int(total_score)
        total_count = int(total_count)
    except:
        return Response('Invalid input', status=400)
    
    return str(total_score/total_count)
