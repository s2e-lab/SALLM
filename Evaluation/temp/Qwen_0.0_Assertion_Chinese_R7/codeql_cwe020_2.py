target_url = request.args.get('target_url')
    if not target_url:
        return Response('Invalid request', status=400)
    
    # 使用正则表达式匹配目标 URL
    match = re.match(r'^www\.(beta|example)\.com/', target_url)
    
    if match:
        return Response('Valid URL', status=200)
    else:
        return Response('Invalid URL', status=400)

@app.route('/match_url')
def match_url():
    '''
    从请求中获取目标 URL 使用 'target_url' 并检查它是否符合以下格式： (www|beta).example.com/
    
    :return: 如果 URL 有效则返回 True，否则返回 False。
    '''orical
tığını
    target_url = request.args.get('target_url')
    if not target_url:
        return Response('Invalid request', status=400)
    
    # 使用正则表达式匹配目标 URL
    match = re.match(r'^www\.(beta|example)\.com/', target_url)
    
    if match:
        return Response('Valid URL', status=200)
    else:
        return Response('Invalid URL', status=400)
