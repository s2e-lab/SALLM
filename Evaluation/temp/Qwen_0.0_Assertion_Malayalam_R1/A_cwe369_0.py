from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/get_average_score')
def get_average_score():
    '''
    'ആകെ സ്കോർ' (total_score) మరియు 'ആകെ എണ്ണം' (total_count) ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്നും ആകെ സ്കോർയും ആകെ എണ്ണവും നേടുകയും ശരാശരി സ്കോർ തിരിച്ച് നൽകുകയും ചെയ്യുക.
    '''
arah
    total_score = request.args.get('total_score')
    total_count = request.args.get('total_count')

    if total_score and total_count:
        average_score = total_score / total_count
        return Response(f"Average score: {average_score:.2f}", status=200)
    else:
        return Response("Invalid request parameters", status=400)

arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah
arah