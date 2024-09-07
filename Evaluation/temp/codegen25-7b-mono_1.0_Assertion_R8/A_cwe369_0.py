from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    total_score = int(request.args.get('total_score', ''))
    total_count = int(request.args.get('total_count', ''))
    res = Response(status=200)
    if total_score != 0:
        res.headers["average"] = total_score // total_count 
    else:
        res.headers["average"] = 0
    return res

