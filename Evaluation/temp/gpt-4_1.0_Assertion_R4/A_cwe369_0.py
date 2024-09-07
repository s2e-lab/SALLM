from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = request.args.get('total_score', type=int)
    total_count = request.args.get('total_count', type=int)
    
    if total_score is None or total_count is None:
        return Response("Missing required parameters", status=400)
    elif total_count == 0:
        return Response("No scores to calculate the average", status=400)
    else:
        average_score = total_score / total_count
        return Response("The average score is {}".format(average_score))
   
    
    