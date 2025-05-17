from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    İsteğin içeriğini 'contents' kullanarak al. 
Dosyanın içeriğini bir sözlük olarak değerlendirerek döndür.
    '''
contents = {
        'title': 'İstek',
        'description': 'İstek hakkında bilgi',
        'content': 'İstek içeriği',
        'author': 'İstek yazarı',
        'date': 'İstek tarihi',
        'tags': 'İstek etiketleri',
        'comments': 'İstek yorumları',
        'likes': 'İstek beğenme sayısı',
        'dislikes': 'İstek beğenme sayısı',
        'views': 'İstek sayfasına gitme sayısı',
        'likes_count': 'İstek beğenme sayısı',
        'dislikes_count': 'İstek beğenme sayısı',
        'views_count': 'İstek sayfasına gitme sayısı',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count': 'İstek yorumları',
        'comments_count':