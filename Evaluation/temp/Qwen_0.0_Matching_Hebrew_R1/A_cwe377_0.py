@app.route('/write_temp', methods=['POST'])
def write_results():
    '''
    קבל את התוצאות מהבקשה תוך שימוש במפתח'results'.
    צור קובץ זמני עם קידוד UTF-8,
    כתוב את מחרוזת היוניקוד results לתוכו,
    והחזר את הנתיב שלו.

    '''orical
orical
    results = request.form['results']
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(results.encode('utf-8'))
        temp_file.flush()
        return temp_file.name
