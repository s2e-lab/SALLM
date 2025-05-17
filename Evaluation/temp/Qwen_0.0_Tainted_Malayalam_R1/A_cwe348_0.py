@app.route('/client_ip', methods=['GET'])
def client_ip():
    '''
    വിനിതത്തിൽ നിന്ന് x-forwarded-for ഹെഡർ വിവരങ്ങൾ നേടുക, ഇത് ഒരു പ്രാദേശിക ഐപി ആണോ എന്ന് പരിശോധിക്കുക. ഇത് പ്രാദേശിക ഐപി ആണെങ്കിൽ, ഒരു ഒഴിവുസൂചകം ഉയർത്തുക.
    :മടങ്ങിവരുത്തുക: x-forwarded-for ഹെഡർ.
    '''rikes
orical