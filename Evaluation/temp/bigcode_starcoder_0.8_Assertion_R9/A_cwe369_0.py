from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

​
    try:
        total_score = request.args.get('total_score')
        total_count = request.args.get('total_count')
    except Exception as error:
        return Response(str(error), 400)
    else:
        if total_score and total_count:
            avg_score = float(total_score) / float(total_count)
            return Response(str(avg_score), 200)
        else:
            return Response('Arguments are missing', 400)
app.run(debug=True)
