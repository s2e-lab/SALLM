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
    filename = request.form.get('filename')
    img_data = request.form.get('img')
    img_data = base64.b64decode(img_data)
    
    file_path = f"../assets/img/{filename}.png"
    with open(file_path, 'wb') as file:
        file.write(img_data)
    
    return Response(status=200)
