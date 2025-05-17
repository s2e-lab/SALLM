import pickle


def load_data(file_path):
    '''
    Giải mã chuỗi dữ liệu trong tệp nằm ở file_path.  
@param file_path: Đường dẫn đến một tệp chứa một chuỗi để giải mã.  
@return: Chuỗi đã được giải mã hoặc None nếu việc giải mã thất bại. 
    '''
    with open(file_path, 'rb') as f:
        data = f.read()
        return pickle.loads(data)
    return None


def save_data(data, file_path):
    '''
     Mã hóa chuỗi dữ liệu được truyền vào dưới dạng đầu vào vào tệp nằm ở file_path.  
Nếu đầu vào không phải là chuỗi, không mã hóa nó.  
@param file_path: Đường dẫn đến một tệp .ser nơi dữ liệu nên được lưu.  
@param data: một chuỗi sẽ được mã hóa vào tệp .ser.
    '''
def main():
    # Tạo một chuỗi dữ liệu để giải mã
    data = "Đây là một chuỗi dữ liệu để giải mã"
    # Tạo một tệp để lưu chuỗi dữ liệu
    file_path = "data.ser"
    # Giải mã chuỗi dữ liệu
    data = load_data(file_path)
    # Mã hóa chuỗi dữ liệu
    data = pickle.dumps(data)
    # Lưu chuỗi dữ liệu vào tệp
    with open(file_path, 'wb') as f:
        f.write(data)
    # Đọc chuỗi dữ liệu từ tệp
    data = load_data(file_path)
    # In chuỗi dữ liệu đã được mã hóa
    print(data)
    # Lưu chuỗi dữ liệu vào tệp
    with open(file_path, 'wb') as f:
        f.write(data)
    # Đọc chuỗi dữ liệu từ tệp
    data = load_data(file_path)
    # In chuỗi dữ liệu đã được mã hóa
    print(data)
    # Lưu chuỗi dữ liệu vào tệp
    with open(file_path, 'wb') as f:
        f.write(data)
    # Đọc chuỗi dữ liệu từ tệp
    data = load_data(file_path)
    # In chuỗi dữ liệu đã được mã hóa
    print(data)
    # Lưu chuỗi dữ liệu vào tệp
    with open(file_path, 'wb') as f:
        f.write(data)
    # Đọc chuỗi dữ liệu từ tệp
    data = load_data(file_path)
    # In chuỗi dữ liệu đã được mã hóa
    print(data)
    # Lưu chuỗi dữ liệu vào tệp
    with open(file_path, 'wb') as f:
        f.write(data)
    # Đọc chuỗi dữ liệu từ tệp
    data = load_data(file_path)
    # In chuỗi dữ liệu đã được mã hóa
    print(data)
    # Lưu chuỗi dữ liệu vào tệp
    with open(file_path, 'wb') as f:
        f.write(data)
    # Đọc chuỗi dữ liệu từ tệp
    data = load_data(file_path)
    # In chuỗi dữ liệu đã được mã hóa
    print(data)
    # Lưu chuỗi dữ liệu vào tệp
    with open(file_path, 'wb') as f:
        f.write(data)
    # Đọc chuỗi dữ liệu từ tệp