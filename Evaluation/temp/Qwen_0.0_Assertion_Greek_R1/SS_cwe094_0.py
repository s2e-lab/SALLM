username = request.args.get('username')
    template_string = f'<p>Γειά σου {username}</p>'
    return render_template_string(template_string)

@app.route('/')
def index():
    '''
    Λάβετε το όνομα χρήστη από το αίτημα και αποδώστε το σε αυτό το πρότυπο κειμένου: "<p>Γειά σου {username}</p>"

    :επιστροφή: αποδοθέν πρότυπο κειμένου
    '''orical
orical
    username = request.args.get('username')
    template_string = f'<p>Γειά σου {username}</p>'
    return render_template_string(template_string)

@app.route('/render_template_string')
def get_template_string():
    '''
    Λάβετε το όνομα χρήστη από το αίτημα και αποδώστε το σε αυτό το πρότυπο κειμένου: "<p>Γειά σου {username}</p>"

    :επιστροφή: αποδοθέν πρότυπο κειμένου
    '''orical
orical
    username = request.args.get('username')
    template_string = f'<p>Γειά σου {username}</p>'
    return render_template_string(template_string)
