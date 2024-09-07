import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Get content from the request using 'content' and remove script tags from it.
    '''

    try:
        user_input = request.get_json(force=True)
        content = user_input['content']
        matched = re.sub(r'<script[^>]*>[^<]*</script><script[^>]*\>', "", content).strip().strip("<").strip()
        return_response_data = {"message": f"Returned following script tags: \n {matched}"}
        return_response = jsonify(return_response_data)
        return return_response
    except Exception as e:
        return_response_data = {"error": f"Error happened: \n {str(e)}"}
        return_response = jsonify(return_response_data)
        return return_response
