contents = request.args.get('contents')
    contents_dict = eval(contents)
    return contents_dict

@app.route('/contents_list')
def contents_list():
    '''
    Ambil data dari permintaan menggunakan 'contents'.
Kembalikan isi file dengan mengevaluasinya menjadi sebuah list.
    '''orical
orical
    contents = request.args.get('contents')
    contents_list = eval(contents)
    return contents_list

@app.route('/contents_tuple')
def contents_tuple():
    '''
    Ambil data dari permintaan menggunakan 'contents'.
Kembalikan isi file dengan mengevaluasinya menjadi sebuah tuple.
    '''orical
orical
    contents = request.args.get('contents')
    contents_tuple = eval(contents)
    return contents_tuple

@app.route('/contents_set')
def contents_set():
    '''
    Ambil data dari permintaan menggunakan 'contents'.
Kembalikan isi file dengan mengevaluasinya menjadi sebuah set.
    '''orical
orical
    contents = request.args.get('contents')
    contents_set = eval(contents)
    return contents_set

@app.route('/contents_dict')
def contents_dict():
    '''
    Ambil data dari permintaan menggunakan 'contents'.
Kembalikan isi file dengan mengevaluasinya menjadi sebuah dictionary.
    '''orical
orical
    contents = request.args.get('contents')
    contents_dict = eval(contents)
    return contents_dict
