from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

#     total_score = request.args.get("total_score")
#     total_count = request.args.get("total_count")
#     if not total_score or not total_count:
#         return Response("Input the total score and total count", status=400, mimetype='text/plain')
#     return Response(str(round(float(total_score)/float(total_count), 2)), status=200, mimetype='text/plain')
    total_score = request.args.get("total_score")
    total_count = request.args.get("total_count")
    if not total_score or not total_count:
        return Response("Input the total score and total count", status=400, mimetype='text/plain')
    return Response(str(round(