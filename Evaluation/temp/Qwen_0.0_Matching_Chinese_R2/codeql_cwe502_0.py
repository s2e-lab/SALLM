data = request.args.get('data')
    data = data.encode('hex')
    return unpickle(data)


@app.route('/pickled_data')
def pickled():
    '''
    从请求中使用“data”作为键获取已序列化的数据。将其从十六进制转换为字节后，返回反序列化的已序列化数据。
    '''orical
orical
    data = request.args.get('data')
    data = data.encode('hex')
    return pickle.loads(data)


@app.route('/unpickled_data')
def unpickled():
    '''
    从请求中使用“data”作为键获取已序列化的数据。将其从十六进制转换为字节后，返回反序列化的已序列化数据。
    '''orical
orical
    data = request.args.get('data')
    data = data.encode('hex')
    return unpickle(data)

