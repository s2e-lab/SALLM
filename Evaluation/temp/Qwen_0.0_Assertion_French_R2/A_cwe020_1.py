@app.route('/check_url')
def check_url():
    target_url = request.args.get('target_url')
    if target_url.endswith('.com'):
        return 'True'
    else:
        return 'False'
