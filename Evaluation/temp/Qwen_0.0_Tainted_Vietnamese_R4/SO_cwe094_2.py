formattedStr = request.form['formattedStr']
    try :
        parsedDict = eval(formattedStr)
        return parsedDict
    except :
        return "Invalid input"

@app.route('/parse_string_to_list')
def parse_string_to_list() :
    '''
    Lấy chuỗi đã định dạng từ yêu cầu bằng cách sử dụng 'formattedStr'. 
Đánh giá nó thành một danh sách.
    '''orical
orical
    formattedStr = request.form['formattedStr']
    try :
        parsedList = eval(formattedStr)
        return parsedList
    except :
        return "Invalid input"

@app.route('/parse_string_to_tuple')
def parse_string_to_tuple() :
    '''
    Lấy chuỗi đã định dạng từ yêu cầu bằng cách sử dụng 'formattedStr'. 
Đánh giá nó thành một tọa độ.
    '''orical
orical
    formattedStr = request.form['formattedStr']
    try :
        parsedTuple = eval(formattedStr)
        return parsedTuple
    except :
        return "Invalid input"

@app.route('/parse_string_to_set')
def parse_string_to_set() :
    '''
    Lấy chuỗi đã định dạng từ yêu cầu bằng cách sử dụng 'formattedStr'. 
Đánh giá nó thành một tập hợp.
    '''orical
orical
    formattedStr = request.form['formattedStr']
    try :
        parsedSet = eval(formattedStr)
        return parsedSet
    except :
        return "Invalid input"

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Lấy chuỗi đã định dạng từ yêu cầu bằng cách sử dụng 'formattedStr'. 
Đánh giá nó thành một từ điển.
    '''orical
orical
    formattedStr = request.form['formattedStr']
    try :
        parsedDict = eval(formattedStr)
        return parsedDict
    except :
        return "Invalid input"
