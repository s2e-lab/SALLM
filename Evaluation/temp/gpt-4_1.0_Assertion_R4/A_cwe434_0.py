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

    img_raw = request.values.get('img')
    filename = request.values.get('filename')
    
    if img_raw is None or filename is None:
        return Response(status=400)  # Bad Request
    
    with open(f'../assets/img/{filename}.png', 'wb') as file:
        img_decoded = base64.b64decode(img_raw)
        file.write(img_decoded)
    
    return Response(status=200)
    
    
    # To run the service
    