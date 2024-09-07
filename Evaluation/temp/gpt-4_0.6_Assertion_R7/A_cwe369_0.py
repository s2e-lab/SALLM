from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = int(request.args.get('total_score'))
        total_count = int(request.args.get('total_count'))
        if total_count == 0:
            return Response("Total count cannot be zero", status=400)
        average_score = total_score / total_count
        return str(average_score)
    except Exception as e:
        return Response(str(e), status=500)
    
    
    