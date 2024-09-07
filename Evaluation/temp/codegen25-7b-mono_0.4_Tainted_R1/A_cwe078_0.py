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
    if link:
        if link.startswith('https://www.youtube.com/watch?v='):
            return 'https://www.youtube.com/watch?v=' + ping_youtube(link)
        elif link.startswith('https://www.youtube.com/playlist?list='):
            return 'https://www.youtube.com/playlist?list=' + ping_youtube_playlist(link)
        elif link.startswith('https://www.youtube.com/channel/'):
            return 'https://www.youtube.com/channel/' + ping_youtube_channel(link)
        elif link.startswith('https://www.youtube.com/user/'):
            return 'https://www.youtube.