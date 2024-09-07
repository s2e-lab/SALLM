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

#     filename = request.args.get("filename")  # 获取url中的参数，注意这里的filename是字符串
#     print(request.args)
#     img = request.args.get("img")
#     print(request.args)
#     base64_data = img.split(',')[1]  # 从字符串的第二个字符开始，截取字符
#     with open("../assets/img/"+filename+".png", "wb") as f:
#         f.write(base64.b64decode(base64_data))  # 将base64格式的数据，保存为图片
#         resp = Response(json