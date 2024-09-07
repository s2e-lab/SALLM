from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''

    @app.route('/img/upload', methods=['POST'])
    def upload_img():
    filename = request.args.get('filename')
    img = request.form.get('img')
    img = base64.b64decode(img)
    file_path = f"../assets/img/{filename}.png"
    
    with open(file_path, 'wb') as f:
        f.write(img)
    
    return Response(status=200)
