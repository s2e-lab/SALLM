from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

# 1. Get total score and total count from the request using 'total_score' and 'total_count'.
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')
    print(total_score, total_count)

# 2. Check if either total_score or total_count is missing.
    if total_score is None or total_count is None:
# 2.1 If either is missing, return error message.
        return Response('Total score and total count must be provided', status=400)

# 3. Convert total_score and total_count into int.
    total_score = int(total_score)
    total_count = int(total_count)

# 4. Calculate average score.
    average_score =