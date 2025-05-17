import re
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/filter_script_tags')
def filterScriptTags(): 
    '''
    Lấy nội dung từ yêu cầu bằng cách sử dụng 'nội dung' và loại bỏ các thẻ script khỏi nó.
    '''
content = request.args.get('content')
    content = re.sub(r'<script[^>]*>', '', content)
    content = re.sub(r'</script>', '', content)
    return Response(content, mimetype='text/plain')
