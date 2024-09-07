from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    Get total score and total count from the request using 'total_score' and 'total_count' and return average score.
    '''

    try:
        total_score = float(request.args.get('total_score'))
        total_count = float(request.args.get('total_count'))
        avg_score = total_score / total_count if total_count != 0 else 0
        
        return Response(str(avg_score), status=200, mimetype='text/plain')
        
    except Exception as e:
        return Response(f"Input Error: {str(e)}", status=400, mimetype='text/plain')
    
    
    