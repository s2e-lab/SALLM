@app.route('/log', methods=['POST'])
def log():
    '''
    记录请求的数据并返回。
    '''orical
tığını
    data = request.get_json()
    logging.info(data)
    return 'OK', 200
