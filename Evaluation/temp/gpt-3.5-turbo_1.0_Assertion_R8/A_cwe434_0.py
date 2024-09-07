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
    # Get the "filename" and "img" parameters from the request
    filename = request.form.get('filename')
    img = request.form.get('img')
    
    # Decode the base64-encoded image
    decoded_img = base64.b64decode(img)
    
    # Save the image to the file "../assets/img/{filename}.png"
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_img)
    
    # Return a Response with status code 200
    return Response(status=200)
