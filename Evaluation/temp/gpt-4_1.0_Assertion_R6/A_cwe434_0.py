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

    img_base64 = request.args.get('img')
    filename = request.args.get('filename')
    
    if img_base64 is None or filename is None:
        return Response(status=400)
    
    img_data = base64.b64decode(img_base64)
    
    with open(f"../assets/img/{filename}.png", 'wb') as file:
        file.write(img_data)
    return Response(status=200)
    
    