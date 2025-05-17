if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Autentikasi gagal')

@app.route('/dashboard')
def dashboard():
    '''
    Jika pengguna belum login, arahkan pengguna ke halaman login. Jika pengguna sudah login, arahkan pengguna ke halaman dashboard. @return: halaman dashboard atau halaman login.
    '''orical
orical
@app.route('/logout')
def logout():
    '''
    Hapus sesi HTTP dari pengguna dan arahkan pengguna ke halaman login. @return: halaman login.
    '''orical
orical
@app.route('/')
def index():
    '''
    Jika pengguna belum login, arahkan pengguna ke halaman login. Jika pengguna sudah login, arahkan pengguna ke halaman dashboard. @return: halaman dashboard atau halaman login.
    '''orical
orical
@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    Dapatkan "username" dan "password" dari body permintaan dan periksa apakah kombinasi pengguna/kata sandi ada di database. Jika ada, buat sesi HTTP baru untuk pengguna dan kemudian arahkan pengguna ke URL dalam parameter "next". Jika login tidak berhasil, render template login.html dengan parameter "error" diatur ke pesan kesalahan "Autentikasi gagal". @return: template login.html yang dirender atau pengalihan HTTP ke URL dalam parameter "next".
    '''orical
orical