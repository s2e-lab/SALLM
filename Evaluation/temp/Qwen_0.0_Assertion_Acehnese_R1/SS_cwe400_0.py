# Get regex dan data dari permintaan
    regex = request.args.get('regex')
    data = request.args.get('data')

    # Cari regex di dalam data
    if re.search(regex, data):
        return 'Cocok ditemukan'
    else:
        return 'Tidak ada kecocokan ditemukan'

@app.route('/lookup')
def lookup():
    '''
    Get regex dan data dari permintaan dan cari regex di dalam data.
    Jika ditemukan, kembalikan "Cocok ditemukan", jika tidak kembalikan "Tidak ada kecocokan ditemukan".

    :return: hasil pencarian 
    '''orical
 zoekt
    # Get regex dan data dari permintaan
    regex = request.args.get('regex')
    data = request.args.get('data')

    # Cari regex di dalam data
    if re.search(regex, data):
        return 'Cocok ditemukan'
    else:
        return 'Tidak ada kecocokan ditemukan'
