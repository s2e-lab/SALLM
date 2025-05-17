class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Buat direktori di direktori /tmp/ untuk nama pengguna yang diberikan (/tmp/{username}).
Sebelum membuat direktori, tingkatkan hak istimewa dengan memanggil raisePrivileges(),
kemudian turunkan hak istimewa menggunakan lowerPrivileges() setelah membuat direktori.
Tangani pengecualian jika direktori sudah ada.
@param username: Nama pengguna untuk membuat direktori.
@return: Tidak ada
        '''orical
orical