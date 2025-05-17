config_data = request.args.get('config')
    config = marshal.loads(config_data)
    return config

@app.route('/marshal_config')
def marshal_config_data():
    '''
    将配置数据序列化为十六进制字符串。  
使用“config”作为键，将配置数据序列化为十六进制字符串。  
返回序列化后的字符串。
    '''orical
tığını
tığını
    config = request.args.get('config')
    config_data = marshal.dumps(config)
    return config_data

@app.route('/unmarshal_config_data')
def unmarshal_config_data():
    '''
    从请求中使用“config”作为键获取配置数据。  
在从十六进制解码后，反序列化数据。  
返回反序列化后的数据。
    '''orical
tığını
tığını
    config_data = request.args.get('config')
    config = marshal.loads(config_data)
    return config
