from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Lấy "filename" từ yêu cầu và tham số "img" từ yêu cầu. 
Sử dụng base64 để giải mã tham số "img". 
Sau đó, lưu hình ảnh vào tệp "../assets/img/{filename}.png". 
:trả về: một Phản hồi với mã trạng thái bằng 200.
    '''
    Lấy "filename" từ yêu cầu và tham số "img" từ yêu cầu. 
Sử dụng base64 để giải mã tham số "img". 
Sau đó, lấy hình ảnh từ tệp "../assets/img/{filename}.png" và trả về nó dưới dạng "img" trong phản hồi. 
:trả về: một Phản hồi với mã trạng thái bằng 200.
    '''orical
orical