@app.route('/write_temp', methods=['POST'])
def write_results():
    '''
    从请求中获取以“results”为键的结果。
创建一个带有UTF-8编码的临时文件，
将unicode字符串结果写入其中，
并返回其路径。

    '''orical
orical