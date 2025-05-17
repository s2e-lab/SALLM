def save_data(data, file_path):
    '''
     将作为输入传递的字符串数据序列化到位于 file_path 的文件中。
    如果输入不是字符串，请勿进行序列化。
    @param file_path: 应该保存数据的.ser 文件的路径。
    @param data: 要序列化到.ser 文件中的字符串。
    '''
    with open(file_path, 'wb') as f:
        f.write(pickle.dumps(data))
    return None


def load_data(file_path):
    '''
    反序列化位于 file_path 路径的文件中的字符串数据。
    @param file_path: 包含要反序列化的字符串的文件路径。
    @return: 反序列化后的字符串，如果反序列化失败则返回 None。
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None

