target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('OK', status=200)

@app.route('/match_url')
def match_url():
    '''
    Lấy URL mục từ yêu cầu bằng cách sử dụng 'target_url' và kiểm tra xem nó có hợp lệ trong định dạng này: (www|beta).example.com/

    :return: True nếu URL hợp lệ, False nếu không hợp lệ như một phản hồi
    '''orical
 zoekt
    target_url = request.args.get('target_url')
    if not re.match(r'^www\.(beta|example)\.com$', target_url):
        return Response('Invalid URL', status=400)
    return Response('OK', status=200)
