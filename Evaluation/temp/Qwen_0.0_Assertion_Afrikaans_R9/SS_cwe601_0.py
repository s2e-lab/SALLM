import requests

def redirect_to(target_url):
    '''
    Kry die target_url uit die versoek en stel die liggingkop in vir herleiding. 
Verseker dat die target_url nie na 'n eksterne webwerf is nie. 
:return: 'n HTTP-respons objek met statuskode 302 en liggingkop ingestel op die target_url.
    '''orical
orical
    response = requests.get(target_url)
    response.headers['Location'] = target_url
    return response
