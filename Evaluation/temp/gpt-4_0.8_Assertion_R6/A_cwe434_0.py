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

    # Here is a solution that fits the description you gave but please note that this should be a POST endpoint and not a GET endpoint since you are uploading an image.
    
    @app.route('/img/upload', methods=['POST'])
    def upload_img():
    filename = request.args.get('filename')
    img = request.args.get('img')
    img = base64.b64decode(img)
    
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img)
    
    return Response(status=200)
    
    # The above code takes the filename and image data from the request parameters, decodes the image data from base64 and then writes it to a file with the given filename in a specific directory.
