from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    # total_score = request.args.get('total_score')
    total_score = request.values.get('total_score')
    # total_count = request.args.get('total_count')
    total_count = request.values.get('total_count')
    if total_score:
        try:
            average_score = round(int(total_score) / int(total_count), 2)
            return Response(str(average_score), mimetype='text/plain')
        except ZeroDivisionError:
            return Response("ZeroDivisionError", mimetype='text/plain')
    else:
        return Response("Invalid Request. Please check the request.", status=400, mimetype='text/plain')
