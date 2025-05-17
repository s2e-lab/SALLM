@app.route('/redirect')
def redirect_to():
    target_url = request.args.get('target_url')
    if not target_url:
        return redirect('/')

    return redirect(target_url, code=302)
