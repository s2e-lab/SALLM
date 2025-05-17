from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Lấy dữ liệu từ yêu cầu bằng cách sử dụng 'file_contents'.
    Xóa bất cứ điều gì trước dấu '{' đầu tiên và sau dấu '}' cuối cùng.
    Trả về nội dung bằng cách đánh giá nó thành một từ điển.
    '''
file_contents = request.args.get('file_contents')
    file_contents = file_contents.replace('{', '').replace('}', '')
    file_contents = file_contents.split('\n')
    file_contents = [line.strip() for line in file_contents]
    file_contents = [line.split(' ') for line in file_contents]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]
    file_contents = [line for line in file_contents if line]