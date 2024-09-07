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

    # filename = request.args.get('filename')
    # img = request.args.get('img')
    # if filename and img:
    #     # base64 decode the "img" and then write to file.
    #     with open('../assets/img/' + filename + '.png', 'wb') as f:
    #         imgdata = base64.b64decode(img)  # base64 decod the "img"
    #         f.write(imgdata)  # write base64 decod img to file
    #     # return success information.
    #     return Response