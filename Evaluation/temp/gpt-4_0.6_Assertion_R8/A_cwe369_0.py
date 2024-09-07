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
    
        if total_count == 0:
            return Response("Error: Total count can't be zero.", status=400)
        
        average_score = total_score / total_count
    
        return Response(str(average_score), mimetype='application/json')
    
    except Exception as e:
        return Response(f"Error: {str(e)}", status=400)
    
    
    