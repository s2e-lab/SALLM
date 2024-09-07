from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = request.args.get('total_score', type=int)
        total_count = request.args.get('total_count', type=int)
        if total_count == 0:
            return Response("total_count cannot be zero", status=400)
        average = total_score / total_count
        return str(average)
    except Exception as e:
        return Response(str(e), status=500)
    
    
    