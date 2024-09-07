import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    link = request.args.get('link')
    url = f"{link}", headers={'User-Agent': '{}'.format(os.environ.get('PING_USER_AGENT', 'Mozilla/5.0'))} )
    _ = requests.get(url).status_code;

    d = ";".join(
        [
            f"PING;{url[0]};{'0';}%;TTL={ttl}" if ttl is not None else f"PING;{url[0]};{'0';}%;TTL={ttl}";
            for ttl in range(10, 200)
        ]
    )
    return d
